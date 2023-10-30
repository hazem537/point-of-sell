from django.db import models
from django.contrib.auth.models import AbstractUser ,BaseUserManager
from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver

class User (AbstractUser):
    class ROLE(models.TextChoices):
        MANGER="MANGER","Manager"
        SUBMANGER ="SUBMANGER","Submanager"
        Employee = "EMPLOYEE","Employee"
    base_role = ROLE.MANGER
    role = models.CharField( max_length=50,choices=ROLE.choices)
    def save(self,*args, **kwargs):
        if not self.role :
            self.role = self.base_role
        return super().save(*args, **kwargs) 
#     employeeee  
class EmployeeManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role = User.ROLE.Employee) 
    
class Employee(User):
    employee = EmployeeManager()
    base_role = User.ROLE.Employee
    class Meta:
        proxy = True         

@receiver(post_save,sender=Employee)
def create_user_profile(sender,instance,created, **kwargs):
    if created and instance.role =="EMPLOYEE":
        EmployeeProfile.objects.create(employee =instance)

class EmployeeProfile(models.Model):
    place = models.ForeignKey("pos.Place", related_name="employee", on_delete=models.CASCADE,null=True ,blank=True)
    employee = models.OneToOneField("Employee",related_name="e_data", on_delete=models.CASCADE)          
    def __str__(self) :
        return self.employee.username

# sub manager
class SubmangerManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs):
        result = super().get_queryset(*args, **kwargs)
        return result.filter(role = User.ROLE.SUBMANGER) 

class SubManager(User):
    submanger = SubmangerManager()
    base_role = User.ROLE.SUBMANGER
    class Meta:
        proxy = True

@receiver(post_save,sender=SubManager)
def create_user_profile(sender,instance,created, **kwargs):
    if created and instance.role =="SUBMANAGER":
        SubmanagerProfile.objects.create(submanager =instance)

class SubmanagerProfile(models.Model):
    place = models.ForeignKey("pos.Place", related_name="submanger", on_delete=models.CASCADE,null=True ,blank=True)
    submanager =models.OneToOneField("SubManager",related_name="s_data", on_delete=models.CASCADE) 
    def __str__(self) -> str:
        return self.submanager.username

# manager 
class ManagerManager(BaseUserManager):
    def get_queryset(self,*args, **kwargs) : 
        result =super().get_queryset(*args, **kwargs)
        return result.filter( role = User.ROLE.MANGER)
class Manager(User):
    manager = ManagerManager()
    base_role = User.ROLE.MANGER
    class Meta :
        proxy = True

class ManagerProfile(models.Model):
    manager = models.OneToOneField("Manager",related_name="m_data", on_delete=models.CASCADE)
    place = models.ForeignKey("pos.Place", related_name="manager", on_delete=models.CASCADE,null=True ,blank=True)
    def __str__(self) -> str:
        return self.manager.username
