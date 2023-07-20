from django.db import models

from bases.models import ClaseModelo

# Create your models here.


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria',
        unique=True
    )

    def __str__(self):
        return '{}'.format(self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = "Categoria"


class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la Categoria',
    )

    def __str__(self):
        return '{}:{}'.format(self.categoria.descripcion, self.descripcion)

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = "Sub Categorias"
        unique_together = ('categoria', 'descripcion')


class Marca(ClaseModelo):
    
    cedula = models.CharField(
        max_length=13,
        help_text='Cedula del Cliente',
        unique=True,
        null=True
    )
    apellido = models.CharField(
        max_length=100,
        help_text='Apellido del cliente',
        null=True
    )
    nombre = models.CharField(
        max_length=100,
        help_text='Nombre del cliente',
        null=True
    )
    direccion = models.CharField(
        max_length=200,
        help_text='Dirección del cliente',
        null=True
    )
    ciudad = models.CharField(
        max_length=100,
        help_text='Ciudad del cliente',
        null=True
    )
    telefono = models.CharField(
        max_length=15,
        help_text='Teléfono del cliente',
        null=True
    )

    def __str__(self):
        return '{}'.format(self.cedula)

    class Meta:
        verbose_name_plural = "Marca"
