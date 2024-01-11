from django.contrib import admin

from home.models import ProductCategory, Product, Basket,PossibleAllergies


admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(PossibleAllergies)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
