from rest_framework import serializers
from .models import Category, Products

class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Products
		fields = ('product_name','product_description','available_quantity','image_path','price')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	products_set = ProductSerializer(many=True,read_only=True)
	class Meta:
		model = Category
		fields = ('products_set','cate_name','cate_id')