from django.urls import path, include
from rest_framework import routers
from .views import UserRegistrationView

router = routers.DefaultRouter()
router.register('users', UserRegistrationView, basename="registration")

urlpatterns = [
    path('', include(router.urls)),
]
