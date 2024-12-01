from django.shortcuts import render
from .serializers import DepartmentSerializer, FeeSerializer, OtherDataSerializer
from rest_framework.decorators import api_view
from rest_framework import status, generics
from rest_framework.response import Response
from.models import Department, Fee, OtherData


@api_view(['GET'])
def DepartmentListView(request):
  departments = Department.objects.all()
  serializer = DepartmentSerializer(departments, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def OtherDataListView(request):
  departments = OtherData.objects.all()
  serializer = OtherDataSerializer(departments, many=True)
  return Response(serializer.data, status=status.HTTP_200_OK)

class LevyByDepartment(generics.ListAPIView):
  serializer_class = FeeSerializer

  def get_queryset(self):
    department_id = self.kwargs["department_id"]
    return Fee.objects.filter(department_id=department_id)
