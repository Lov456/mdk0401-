from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EquipmentOrderViewSet

router = DefaultRouter()
router.register(r"orders", EquipmentOrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
]