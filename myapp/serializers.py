from django.db.models import fields
from rest_framework import serializers
from .models import Product
class ProductSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model=Product
        fields=('id','name','description','price','image')
