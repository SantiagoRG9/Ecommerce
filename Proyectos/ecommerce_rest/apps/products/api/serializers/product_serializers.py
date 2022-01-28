from rest_framework import serializers

from apps.products.models import Product
# from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state','created_date', 'delete_date', 'modified_date')

    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar unidad de medida")
        return value

    def validate_category_product(self,value):
        if value == '' or value == None:
            raise serializers.ValidationError("Debe ingresar una categoria de producto")
        return value

    def validate(self, data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({
                "measure_unit":"Debe ingresar unidad de medida"
                })

        if 'category_product' not in data.keys():
            raise serializers.ValidationError({
                "category_products":"Debe ingresar una categoria de producto"
                })

        return data

    def to_representation(self, instance):
        return{
            "id" : instance.id,
            "name" : instance.name,
            "description" : instance.description,
            "image" : instance.image.url if instance.image != '' else '',
            "measure_unit" : instance.measure_unit.description if instance.measure_unit is not None else '',
            "category_product" : instance.category_product.description if instance.category_product is not None else '',
        }