from rest_framework import serializers
from .models import  Employee  ,SubManager , Manager ,User  ,EmployeeProfile,SubmanagerProfile,ManagerProfile
class employeeProfileSer(serializers.ModelSerializer):
    place =serializers.StringRelatedField(source="place.name" )
    class Meta :
        model = EmployeeProfile
        fields = ['place']

class employeeSer(serializers.ModelSerializer):
    data = employeeProfileSer( source  = "e_data",read_only = True)
    class Meta:
        model  = Employee
        fields= ["id","username", "password","data"]

    def create(self, validated_data):
        new = Employee.objects.create_user(username = validated_data["username"] ,password = validated_data["password"])
        return new    

class submangerProfileSer(serializers.ModelSerializer):
    place =serializers.StringRelatedField(source="place.name" )
    class Meta :
        model = SubmanagerProfile
        fields = ['place']

class  SubmangerSer(serializers.ModelSerializer):
    data = employeeProfileSer( source  = "s_data",read_only = True)
    class Meta:
        mdoel = SubManager
        fields = fields= ["username", "password","data"]

    def create(self, validated_data):
        new = SubManager.objects.create_user(username = validated_data["username"] ,password = validated_data["password"])
        return new    
    

class mangerProfileSer(serializers.ModelSerializer):
    place =serializers.StringRelatedField(source="place.name" )
    class Meta :
        model = ManagerProfile
        fields = ['place']

class  SubmangerSer(serializers.ModelSerializer):
    data = employeeProfileSer( source  = "m_data",read_only = True)
    class Meta:
        mdoel = SubManager
        fields = fields= ["username", "password","data"]

    def create(self, validated_data):
        new = Manager.objects.create_user(username = validated_data["username"] ,password = validated_data["password"])
        return new    
    