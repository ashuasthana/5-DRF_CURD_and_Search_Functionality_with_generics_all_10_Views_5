from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status

# Basic Employee List View API for show all resoures
class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer 

# Employee List View with Search Operation
class EmployeeSearchAPIView(ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer 
    #Search operation(http://127.0.0.1:8000/api/?search=As)
    def get_queryset(self):
        name=self.request.GET.get('search')
        if name is not None:
            # qs=Employee.objects.filter(ename__icontains=name)
            qs=self.queryset.filter(ename__icontains=name)
            return qs  
        return self.queryset
        
# Create your Create API View for Create new resources here.
class EmployeeCreateAPIView(CreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer   

# Create your Update API View for Update existing resources here.
class EmployeeUpdateAPIView(UpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer   

# Create your Destoryviews delete resources here.
class EmployeeDestroyAPIView(DestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer          

# Create your Destory API View for delete resources here.
class EmployeeRetrievePIView(RetrieveAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer       

# Create your List Create API View Both
class EmployeeListCreateAPIView(ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer     

# Create your Retrieve Update API View Both
class EmployeeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer     

# Create your Retrieve Destory API View Both
class EmployeeRetrieveDestoryAPIView(RetrieveDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer     

# Create your Retrieve Update Destory API View 
class EmployeeRetrieveUpdateDestoryAPIView(RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer  
    lookup_field='id'   