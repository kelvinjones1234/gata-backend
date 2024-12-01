from django.db import models
from payment_app .models import Department, Fee
from user_app.models import User



class Transaction(models.Model):
  matriculation_number = models.ForeignKey(User, on_delete=models.CASCADE)
  full_name = models.CharField(max_length=100)
  email = models.EmailField(null=True, blank=True)
  department = models.ForeignKey(Department, on_delete=models.CASCADE)
  fee = models.ForeignKey(Fee, on_delete=models.CASCADE)
  amount = models.CharField(max_length=50)
  level = models.CharField(max_length=100, blank=True, null=True)
  semester = models.CharField(max_length=100, blank=True, null=True)
  date = models.DateTimeField(auto_now_add=True)
  paid = models.BooleanField(default=False)
  reference_number = models.CharField(max_length=50)

  def __str__(self):
    return f'{self.matriculation_number}' 
  






