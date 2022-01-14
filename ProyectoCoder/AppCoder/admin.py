from django.contrib import admin
from AppCoder.models import Cursos, Entregables, Estudiantes, Profesores

# Register your models here.

admin.site.register(Cursos)
admin.site.register(Entregables)
admin.site.register(Estudiantes)
admin.site.register(Profesores)

