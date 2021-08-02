from rest_framework import viewsets
from .serializers import ProductSerializer, ProductCategorySerializer, ProductTypeSerializer, StandardSerializer, StandardCategorySerializer, StandardRequirementSerializer, KeyWordSerializer
from .models import Product, ProductCategory, ProductType, Standard, StandardRequirement, StandardCategory, KeyWords

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Product

class ProductTypeViewSet(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

class StandardViewSet(viewsets.ModelViewSet):
    queryset = Standard.objects.all()
    serializer_class = StandardSerializer

class StandardRequirementViewSet(viewsets.ModelViewSet):
    queryset = StandardRequirement.objects.all()
    serializer_class = StandardRequirementSerializer

class StandardCategoryViewSet(viewsets.ModelViewSet):
    queryset = StandardCategory.objects.all()
    serializer_class = StandardCategorySerializer

class KeyWordViewSet(viewsets.ModelViewSet):
    queryset = KeyWords.objects.all()
    serializer_class = KeyWordSerializer
