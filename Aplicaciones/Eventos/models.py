from django.db import models

# Create your models here.
class Evento(models.Model):
    CATEGORIAS = [
        ('RE', 'Recreativo'),
        ('CU', 'Cultural'),
        ('DE', 'Deportivo'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    fecha = models.DateField()
    hora = models.TimeField()
    ubicacion = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)  # Activo o no

    def __str__(self):
        fila="{0}: {1} {2}"
        return fila.format(self.titulo, self.descripcion, self.categoria)

class Registro(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    nombre_participante = models.CharField(max_length=100)
    email = models.EmailField()
    registrado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre_participante} - {self.evento.titulo}"