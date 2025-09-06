# gestion/models.py
from django.db import models
from django.utils import timezone

class Medico(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Dr. {self.nombre} ({self.especialidad})"

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    direccion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    ESTADO_CHOICES = [
        ('programada', 'Programada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name="citas")
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name="citas")
    fecha_hora = models.DateTimeField(default=timezone.now)
    motivo = models.CharField(max_length=255)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='programada')

    def __str__(self):
        return f"Cita de {self.paciente.nombre} con Dr. {self.medico.nombre} el {self.fecha_hora.strftime('%d/%m/%Y %H:%M')}"