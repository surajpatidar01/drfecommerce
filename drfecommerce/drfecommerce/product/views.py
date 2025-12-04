# from drf_spectacular.utils import extend_schema
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import  action
# from .models import Product,Brand,Category
# from .serializers import CategorySerializer,BrandSerializer,ProductSerializer
#
#
#
# class ProductViewSet(viewsets.ViewSet):
#
#     queryset = Product.objects.all()
#     @action(detail=False,
#             methods=['get'],
#             url_path=r"category/(?P<category>\w+)/all")
#     def list_products_by_category(self,request,category=None):
#         serialized=ProductSerializer(Product.objects.filter(category_name=Category))
#         return Response(serialized.data)
#
#
#     serializer_class = ProductSerializer
#     @extend_schema(request=CategorySerializer)
#     def list(self,request):
#
#         serializer_class = ProductSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)
#
#
#
# class BrandViewSet(viewsets.ViewSet):
#     queryset = Brand.objects.all()
#     serializer_class=BrandSerializer
#     @extend_schema(request=BrandSerializer)
#     def list(self,request):
#         queryset = Brand.objects.all()
#         serializer_class = BrandSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)
#
#
# class CategoryViewSet(viewsets.ViewSet):
#     queryset = Category.objects.all()
#
#
#     serializer_class=CategorySerializer
#     @extend_schema(request=CategorySerializer)
#     def list(self,request):
#         queryset = Category.objects.all()
#         serializer_class = CategorySerializer(self.queryset,many=True)
#         return Response(serializer_class.data)




from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, Brand, Category
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer


class ProductViewSet(viewsets.ViewSet):

    @action(detail=False,
            methods=['get'],
            url_path=r"category/(?P<category>\w+)/all")
    def list_products_by_category(self, request, category=None):
        products = Product.objects.filter(category__name=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        queryset = Brand.objects.all()
        serializer = BrandSerializer(queryset, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ViewSet):

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)
