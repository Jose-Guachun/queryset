from django.db import models

class Marca(models.Model):

    descripcion = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.descripcion

class Modelo(models.Model):

    descripcion = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.descripcion


class Producto(models.Model):

    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    descripcion = models.CharField(max_length=100)
    fecha=models.DateTimeField()
    cantidad=models.IntegerField()
    precio=models.DecimalField(max_digits=8,decimal_places=2)
    total=models.DecimalField(max_digits=8,decimal_places=2)


    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.descripcion

