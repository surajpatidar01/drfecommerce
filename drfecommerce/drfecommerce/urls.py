
import sys
import os
from django.contrib import admin
from django.urls import path,include
from django.urls import path
from rest_framework.routers import DefaultRouter
from drfecommerce.product.views import ProductViewSet, BrandViewSet, CategoryViewSet
from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView
from drf_spectacular.utils import extend_schema



router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'categories', CategoryViewSet, basename='category')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),

    path('api/schema/',SpectacularAPIView.as_view(),name='schema'),
    path('api/schema/swagger-ui/',SpectacularSwaggerView.as_view(),name='swagger-ui'),


]