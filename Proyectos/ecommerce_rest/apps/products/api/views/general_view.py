
from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, IndicatorSerializer, CategoryProductSerializer
from apps.base.api import GeneralListApiView
from apps.products.models import MeasureUnit

from rest_framework import viewsets

class MeasureUnitViewSet(viewsets.GenericViewSet):
    """
    Hola desde unidad de medida
    """
    model = MeasureUnit
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
        Retorna unidades de medida disponibles


        Params, 
        name --> Nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)

    
class IndicatorViewSet(viewsets.GenericViewSet):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def list(self, request):
        """
        Retorna unidades de medida disponibles


        Params, 
        name --> Nombre de la unidad de medida
        """
        data = self.get_queryset()
        data = self.get_serializer(data, many = True)

class CategoryProductViewSet(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer




# class MeasureUnitListAPIView(viewsets.ModelViewSet):
#     serializer_class = MeasureUnitSerializer

    
# class IndicatorListAPIView(viewsets.ModelViewSet):
#     serializer_class = IndicatorSerializer


# class CategoryProductListAPIView(viewsets.ModelViewSet):
#     serializer_class = CategoryProductSerializer

