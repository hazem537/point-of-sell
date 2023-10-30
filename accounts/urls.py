from rest_framework import routers
from .views import employeeViewset
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
router = routers.SimpleRouter()
router.register("employee", employeeViewset,"employee")
urlpatterns=[
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]
urlpatterns += router.urls 