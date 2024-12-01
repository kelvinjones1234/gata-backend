from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer, GetTransactionSerializer, TransactionSummarySerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import Transaction, Fee
from .serializers import TransactionSummarySerializer


class TransactionView(APIView):
    def post(self, request):
        ref_number = request.data.get('reference_number')
        if ref_number and Transaction.objects.filter(reference_number=ref_number).exists():
            # If the ref_number exists, return a success response but do not save
            return Response({'detail': 'Transaction with this reference number already exists.'}, status=status.HTTP_200_OK)
        
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class GetUserTransactions(generics.ListAPIView):
  serializer_class = GetTransactionSerializer
  permission_classes = [IsAuthenticated]

  def get_queryset(self):
    return Transaction.objects.filter(matriculation_number=self.request.user.id)


class TransactionRetrieveView(generics.RetrieveAPIView):
  queryset = Transaction.objects.all()
  serializer_class = TransactionSerializer

  def get_object(self):
    reference_number = self.kwargs['reference_number']
    return get_object_or_404(Transaction, reference_number=reference_number)



class UserSummaryView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view

    def get(self, request):
        user = request.user  # Get the logged-in user
        
        # Transaction Summary
        transactions = Transaction.objects.filter(matriculation_number=user)
        total_transaction_sum = transactions.aggregate(total_amount=Sum('amount'))['total_amount'] or 0
        
        # Fee Summary (based on the user's department)
        department = user.department  # Assuming `User` model has a `department` ForeignKey
        total_fee_sum = Fee.objects.filter(department=department).aggregate(total_amount=Sum('amount'))['total_amount'] or 0

        # Fees not in Transactions
        paid_fee_ids = transactions.values_list('fee_id', flat=True)
        unpaid_fees = Fee.objects.filter(department=department).exclude(id__in=paid_fee_ids)

        unpaid_fees_list = [
            {"fee": fee.fee, "amount": fee.amount} for fee in unpaid_fees
        ]

        # Prepare data for response
        data = {
            "user": {
                "full_name": user.full_name,  # Assuming `full_name` is a field on your User model
                "department": department.department,
            },
            "transaction_summary": {
                "total_transactions": total_transaction_sum,
                "transaction_count": transactions.count(),
                "total_fees": total_fee_sum,
                "unpaid_fees": unpaid_fees_list,
            },
            # "fee_summary": {
            #     "total_fees": total_fee_sum,
            #     "unpaid_fees": unpaid_fees_list,
            # },
        }

        # Use a serializer for response (optional)
        serializer = TransactionSummarySerializer(data)
        return Response(serializer.data, status=200)
