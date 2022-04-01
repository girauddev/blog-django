from django.db import models

#Creamos modelos de productos que venderemos en la plataforma

#Creamos objeto mouse
class Mouse(models.Model):
    id =            models.AutoField(primary_key=True) #Agrego un campo de auto completado para asignar un identificador de objeto unico
    nombre =        models.CharField(max_length=60)
    marca =         models.CharField(max_length=40)
    modelo =        models.CharField(max_length=40)
    color =         models.CharField(max_length=40)
    descripcion =   models.CharField(max_length=120)

# Creamos objeto monitor
class Display(models.Model):
    id =            models.AutoField(primary_key=True) #Agrego un campo de auto completado para asignar un identificador de objeto unico
    nombre =        models.CharField(max_length=60)
    marca =         models.CharField(max_length=40)
    modelo =        models.CharField(max_length=40)
    color =         models.CharField(max_length=40)
    pulgadas =      models.CharField(max_length=40)
    resolucion =    models.CharField(max_length=40)
    descripcion =   models.CharField(max_length=120)

#Creamos objeto auriculares
class Headphone(models.Model):
    id =            models.AutoField(primary_key=True) #Agrego un campo de auto completado para asignar un identificador de objeto unico
    nombre =        models.CharField(max_length=60)
    marca =         models.CharField(max_length=40)
    modelo =        models.CharField(max_length=40)
    color =         models.CharField(max_length=40)
    sonido =        models.CharField(max_length=40)
    descripcion =   models.CharField(max_length=120)
