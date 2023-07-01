from django.urls import path
from .views import BranchList, BranchDetail, EmployeeList, EmployeeDetail
from django.urls import path, include


urlpatterns = [
    path('api/', include('employees.urls')),
    path('api/employees/', EmployeeList, name='employee_list'),
]
urlpatterns = [
    path('branches/', BranchList.as_view()),
    path('branches/<int:pk>/', BranchDetail.as_view()),
    path('employees/', EmployeeList.as_view()),
    path('employees/<int:pk>/', EmployeeDetail.as_view()),
]