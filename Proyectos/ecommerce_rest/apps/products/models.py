from pyexpat import model
from unittest.mock import Base
from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel

class MeasureUnit(BaseModel):

    description = models.CharField('Descripcion', max_length=50, blank=False,null=False, unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Unidad de medida"
        verbose_name_plural = "Unidades de medidas"

    def __str__(self):
        return self.description


class CategoryProduct(BaseModel):

    description = models.CharField('Descripcion', max_length=50, unique=True, null=False, blank=False)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categorias de Productos"

    def __str__(self):
        return self.description

class Indicator(BaseModel):

    descount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, verbose_name='Indicador de Oferta')
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'Oferta de la Categoria{self.category_product} : {self.descount_value}%'


class Product(BaseModel):
    """Model definition for Product."""

    # TODO: Define fields here

    name = models.CharField('Nombre de producto', max_length=50, unique=True,blank = False, null=False)
    description = models.TextField('Descripcion de Producto', blank=False, null=False)
    image = models.ImageField('Imagen del producto', upload_to='products/', blank=True, null = True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


   

