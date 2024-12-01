from rest_framework import serializers
from .models import Department, Fee, OtherData

class DepartmentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Department
    fields = '__all__'


class FeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fee
    fields = '__all__'

class OtherDataSerializer(serializers.ModelSerializer):
  class Meta:
    model = OtherData
    fields = '__all__'