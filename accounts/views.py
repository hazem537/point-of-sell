from rest_framework import viewsets
from .serializer import employeeSer 
from .models import Employee
# from rest_framework.permissions import IsAuthenticated

class employeeViewset(viewsets.ModelViewSet):
    # permission_classes =[IsAuthenticated] 
    model = Employee
    serializer_class = employeeSer
    queryset = Employee.employee.all()
    
