from rest_framework import serializers
from .models import Branch, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'age', 'email', 'phone_number', 'branch']

class BranchSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Branch
        fields = ['id', 'name', 'building_number', 'street', 'area', 'city', 'country', 'manager', 'employees']