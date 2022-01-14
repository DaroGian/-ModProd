from django.db import models

class Cursos(models.Model):

    nombre = models.CharField('nombre', max_length=50)
    camada = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    

class Estudiantes(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    email = models.EmailField()

class Profesores(models.Model):
    nombre = models.CharField('nombre', max_length=50)
    apellido = models.CharField('apellido', max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregables(models.Model):
    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()

class cursoform(models.Model):
    curso = models.CharField(max_length=30)
    camada = models.IntegerField()