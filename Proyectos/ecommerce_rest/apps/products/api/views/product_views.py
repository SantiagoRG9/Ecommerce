from itertools import product
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer

class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    # CONSULTA o queryset
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)


class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    # CONSULTA o queryset
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()

    def patch(self,request,pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializers = self.serializer_class(self.get_queryset(pk))
            return Response(product_serializers.data, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)