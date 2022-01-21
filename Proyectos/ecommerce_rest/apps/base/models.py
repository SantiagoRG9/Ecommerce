from django.db import models

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    created_date = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    modified_date = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:

        abstract = True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Base'


    # def get_absolute_url(self):
    #     return reverse("BaseModel_detail", kwargs={"pk": self.pk})

