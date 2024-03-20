# Create your models here.
from typing import Any
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class program(models.Model):
    id= models.AutoField(primary_key=True)
    especialidad= models.CharField(max_length=100, verbose_name='Especialiad')
    imagen= models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null=True)
    descripcion= models.TextField(verbose_name="Descripcion",null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        fila= "Especialidad" + self.especialidad+ "-"+"Descripcion"+ self.descripcion
        return fila
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
        

