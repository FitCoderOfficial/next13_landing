from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register("upload", views.FoodViewSet)
router.register("foodchoice", views.FoodChoiceViewSet)



urlpatterns = [
    path("", include(router.urls)),
]