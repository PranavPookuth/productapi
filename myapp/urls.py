from os.path import basename

from django.urls import path, include
from .views import ProductViewSet,ProductdetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', ProductViewSet,basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('Products/', ProductdetailViewSet.as_view(), name='Productdetail'),
]
