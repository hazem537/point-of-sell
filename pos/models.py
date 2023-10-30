from django.db import models
from django.db.models.query import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
from rest_framework import status 
from django.db.models import Sum
# /////////////////////////////////////////////////////////////
class Product(models.Model):
    name = models.CharField( max_length=50 ,unique=True)
    supplyer = models.ForeignKey("Supplyer", related_name="product", on_delete=models.CASCADE)

class Place (models.Model):
    name  = models.CharField( max_length=50)
    class ROLE(models.TextChoices):
        STORE ="STORE",'Store'
        PORT = "PORT","Port"
        SUPPLYER ="SUPPLYER","Supplyer"
    role = models.CharField( max_length=50,choices=ROLE.choices)   
    base_role = ROLE.STORE

    def save(self, *args, **kwargs):
        if  not self.role:
            self.role = self.base_role 
        return super().save(*args, **kwargs)     
    def __str__(self) -> str:
        return self.name
    
class StoreManager(models.Manager):
    def get_queryset(self,*args, **kwargs) -> QuerySet:
        result =  super().get_queryset(*args, **kwargs) 
        return result.filter(role = Place.ROLE.STORE)   
class PortManager(models.Manager):
    def get_queryset(self,*args, **kwargs) -> QuerySet:
        result =  super().get_queryset(*args, **kwargs) 
        return result.filter(role = Place.ROLE.PORT)
class SupplyerManager(models.Manager):
    def get_queryset(self,*args, **kwargs) -> QuerySet:
        result= super().get_queryset(*args, **kwargs)
        return result.filter(role = Place.ROLE.SUPPLYER)       
    
class Supplyer(Place):
    supplyer = SupplyerManager()
    base_role = Place.ROLE.SUPPLYER
    class Meta:
        proxy = True    

class Store(Place):
    store = StoreManager()
    base_role = Place.ROLE.STORE
    class Meta:
        proxy =True
    pass
class Port (Place):
    port = PortManager()
    base_role = Place.ROLE.PORT
    class Meta:
        proxy =True
    pass

class StoreProfile(models.Model):
    store = models.OneToOneField("Store", related_name="s_detail", on_delete=models.CASCADE)

    @property
    def get_all_product_exist(self):
        return ProductDetail.objects.filter(place = self.id)
    
    pass    
class PortProfile(models.Model):
    profile =models.OneToOneField("Port", related_name="p_detail", on_delete=models.CASCADE)

    pass
class SupplyerProfile(models.Model):
    supplyer = models.OneToOneField("Supplyer", related_name="sup_detail", on_delete=models.CASCADE)

    pass


class ProductDetail(models.Model):
    product = models.ForeignKey("Product", related_name="detail" ,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default = 0)
    place  = models.ForeignKey("Place",related_name="contain", on_delete=models.CASCADE)
    @property
    def get_amount(self):
        get_in = Transaction.objects.filter(product = self.product ,reciver = self.place).aggregate(Sum('amount'))
     
        get_out = Transaction.objects.filter(product = self.product ,sender = self.place).aggregate(Sum('amount'))
        return get_in['amount__sum'] - get_out['amount__sum']
        
    @property 
    def last_buy_price (self):
        max_date  =Transaction.objects.latest("date").date
        trans = Transaction.objects.get(date =max_date , product = self.product)
        return trans.price
        
class Transaction (models.Model):
    product = models.ForeignKey("Product", related_name="trans" ,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    price = models.DecimalField( max_digits=5, decimal_places=2)
    sender = models.ForeignKey("Place",related_name="get_out", on_delete=models.CASCADE)
    reciver = models.ForeignKey("Place", related_name="get_in", on_delete=models.CASCADE)
    date = models.DateField( auto_now=True)
    @property
    def total(self):
        return self.amount *self.price
    def save(self,*args, **kwargs):
        #  get sender  prod detail
         # if sender  is port or store  check amount is enough 
        #   minus amount from detail 
        detail = False
        if self.sender.role  == Place.ROLE.PORT or  self.sender.role  == Place.ROLE.STORE :
            try:
                detail = ProductDetail.objects.get(place = self.sender ,product = self.product ) 
            except ProductDetail.DoesNotExist:
                print("not exist")    
            if detail :
                if detail.amount>self.amount:
                    detail.amount -=self.amount 
                    detail.save()           
                else: 
                    return Response({"message":"not enough amount "},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message":"not enough amount "},status=status.HTTP_400_BAD_REQUEST)
        if (self.reciver.role  == Place.ROLE.PORT) or  (self.reciver.role  == Place.ROLE.STORE) :

            detail,_ = ProductDetail.objects.get_or_create(place = self.reciver ,product = self.product ) 
            detail.amount +=self.amount 
            detail.save()           
        # get reciver prod detail 
        # if reciver is port or store 
        #   add amount to it detail 
        # add 
        return super().save(*args, **kwargs)    
