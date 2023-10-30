from rest_framework import routers
from .views import join
from django.urls import path
router = routers.SimpleRouter()
urlpatterns=[
    path("addemp/",join.as_view())
]
urlpatterns += router.urls
