from itertools import product
from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializers import ProductSerializer


# ------------------------------------CRUD VIEWSET ROUTERS UNA CLASE PARA CRUD------------------------------

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self,request):
        product_serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(product_serializer.data, status=status.HTTP_200_OK)

    # DENTRO DE ViewSet NO SE LLAMA post CAMBIA POR create
    def create(self, request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id = pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error':'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)







# ---------------------------------------------CRUD URLS-------------------------------------

# class ProductCreateListAPIView(generics.ListCreateAPIView):
#     serializer_class = ProductSerializer
#     queryset = ProductSerializer.Meta.model.objects.filter(state = True)

#     def post(self, request):
#         serializer = self.serializer_class(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message' : 'Producto creado correctamente!'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializer

#     # CONSULTA o queryset
#     def get_queryset(self, pk=None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.filter(state = True)
#         else:
#             return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

#     def patch(self,request,pk=None):
#         product = self.get_queryset(pk)
#         if product:
#             product_serializers = self.serializer_class(self.get_queryset(pk))
#             return Response(product_serializers.data, status=status.HTTP_200_OK)
#         return Response({'error':'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

    # def put(self, request, pk=None):
        # if self.get_queryset(pk):
        #     product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
        #     if product_serializer.is_valid():
        #         product_serializer.save()
        #         return Response(product_serializer.data, status=status.HTTP_200_OK)
        #     return Response(product_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    # def delete(self, request, pk=None):
    #     product = self.get_queryset().filter(id = pk).first()
    #     if product:
    #         product.state = False
    #         product.save()
    #         return Response({'message':'Producto eliminado correctamente!'}, status=status.HTTP_200_OK)
    #     return Response({'error':'No existe un producto con estos datos'}, status = status.HTTP_400_BAD_REQUEST)


    # class ProductListAPIView(GeneralListApiView):
    #     serializer_class = ProductSerializer