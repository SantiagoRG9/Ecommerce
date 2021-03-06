from django.urls import path

from apps.products.api.views.general_view import MeasureUnitListAPIView, IndicatorListAPIView, CategoryProductListAPIView
from apps.products.api.views.product_viewsets import (
     ProductCreateListAPIView, ProductRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('measure_unit/', MeasureUnitListAPIView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorListAPIView.as_view(), name='indicator'),
    
    # path('category_product/', CategoryProductListAPIView.as_view(), name='category_product'), 
    # path('product/', ProductCreateListAPIView.as_view(), name='product_create_list'),
    # path('product/retrieve-update-destroy/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),
]
