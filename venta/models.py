from django.db import models

# Create your models here.
class Cliente(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=100, null=False)
    correo = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.rut+" "+self.nombre

class Producto(models.Model):
    codigo = models.PositiveIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    precio = models.PositiveIntegerField(default=0)
    stock  = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.codigo)+ " "+self.nombre

class Detalle(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.producto.nombre)+" "+str(self.cantidad)

class Documento(models.Model):
    numero = models.PositiveIntegerField(primary_key=True)
    tipo   = models.CharField(max_length=30, null=False)
    fecha  = models.DateField(null=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalles = models.ManyToManyField(Detalle)



