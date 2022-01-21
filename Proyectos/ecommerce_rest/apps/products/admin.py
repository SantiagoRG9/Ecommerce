from django.contrib import admin
from apps.products.models import *

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')


class CategoryProductUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')

admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductUnitAdmin)
admin.site.register(Indicator)
admin.site.register(Product)