from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import ProductSerializer, StandardSerializer


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def standards(request):
    keywords = KeyWords.objects.get()
    standards = Standard.objects.all()
    serializer = StandardSerializer(standards, many=True)

    return Response(serializer.data)
