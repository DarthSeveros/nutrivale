from django.db import models

# Create your models here.

MODALIDAD = (
    ("ONLINE", "Online"),
    ("PRESENCIAL", "Presencial")
)

ESTADO_CONSULTA = (
    ("ANULADA", "Anulada"),
    ("REALIZADA", "Realizada"),
    ("PENDIENTE", "Pendiente")
)

DIAGNOSTICO = (
    ("ENFLAQUECIDO", "Enflaquecido"),
    ("NORMAL", "Normal"),
    ("SOBREPESO", "Sobrepeso"),
    ("OBESIDAD GRADO I", "Obesidad grado I"),
    ("OBESIDAD GRADO II", "Obesidad grado II")
)

TIPO_CONSULTA =(
    ("INGRESO", "Ingreso"),
    ("CONTROL", "Control")
)
HOURS = (
    ("10:00", "10:00"),
    ("11:00", "11:00"),
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00")
)      

class Paciente(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    apellido = models.CharField(max_length=100, verbose_name="Apellido")
    rut = models.CharField(max_length=20, verbose_name="RUT")
    patologias = models.CharField(max_length=150, verbose_name="Patologías", blank=True)
    active = models.BooleanField()

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class DatosPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    diagnostico = models.CharField(max_length=100, choices=DIAGNOSTICO, verbose_name="Diagnóstico nutricional")
    peso = models.PositiveIntegerField()
    talla = models.PositiveIntegerField()
    imc = models.PositiveIntegerField()
    active = models.BooleanField()

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente", limit_choices_to={'active': True})
    fecha = models.DateField(verbose_name="Fecha consulta")
    hora = models.CharField(max_length=11, choices=HOURS, verbose_name="Hora", unique_for_date="fecha", 
    error_messages= {'unique_for_date': "La hora no está disponible"}
    )
    
    tipo = models.CharField(max_length=100, choices=TIPO_CONSULTA,verbose_name="Tipo consulta")
    modalidad = models.CharField(max_length=20, choices=MODALIDAD, verbose_name="Modalidad")
    estado = models.CharField(max_length=100, choices=ESTADO_CONSULTA, verbose_name="Estado")
    active = models.BooleanField()

    def __str__(self):
        return f'{self.paciente}'



    
