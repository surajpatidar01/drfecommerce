from django.contrib import admin

from .models import Brand,Product,Category,ProductLine

class ProductInLineAdmin(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInLineAdmin
    ]



admin.site.register(Category)
admin.site.register(Brand)



