from rest_framework import serializers
from .models import Product, ProductType, ProductCategory, Standard, StandardCategory, StandardRequirement, KeyWords


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__',


class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = '__all__'


class StandardRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardRequirement
        fields = '__all__'


class StandardCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardCategory
        fields = '__all__'


class KeyWordSerializer(serializers.ModelSerializer):
    name = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title')

    class Meta:
        model = KeyWords
        fields = '__all__'
