from django.shortcuts import render
from rest_framework import generics
from .models import Branch, Employee
from .serializers import BranchSerializer, EmployeeSerializer
from django.http import JsonResponse
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all()
    data = {'employees': list(employees.values())}
    return JsonResponse(data)

class BranchList(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
# Create your views here.
