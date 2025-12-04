from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product,Brand,Category
from .serializers import CategorySerializer,BrandSerializer,ProductSerializer



class ProductViewSet(viewsets.ViewSet):

    serializer_class=ProductSerializer
    @extend_schema(request=CategorySerializer)
    def list(self,request):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer(queryset,many=True)
        return Response(serializer_class.data)



class BrandViewSet(viewsets.ViewSet):
    serializer_class=BrandSerializer
    @extend_schema(request=BrandSerializer)
    def list(self,request):
        queryset = Brand.objects.all()
        serializer_class = BrandSerializer(queryset,many=True)
        return Response(serializer_class.data)


class CategoryViewSet(viewsets.ViewSet):
    serializer_class=CategorySerializer
    @extend_schema(request=CategorySerializer)
    def list(self,request):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer(queryset,many=True)
        return Response(serializer_class.data)


