from django.shortcuts import render
from rest_framework import viewsets
from pos.models import  Place
from accounts.models import EmployeeProfile
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from pos.serializer import JoinEmployeeToPlace
    

class join (generics.UpdateAPIView ):
    serializer_class = JoinEmployeeToPlace
    def update(self,request ,*args, **kwargs):
        print(request.data)
        serializer = JoinEmployeeToPlace(data = request.data)
        serializer.is_valid(raise_exception=True)
        emp = EmployeeProfile.objects.get(employee =serializer.validated_data["employee_id"])
        # place
        emp.place =Place.objects.get(id =serializer.validated_data["place_id"] )
        emp.save()
        # employee or sub manger
        return Response({"message":"update done"},status=status.HTTP_200_OK)
    

