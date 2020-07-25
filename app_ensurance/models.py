from django.db import models


class plan(models.Model):
    nombre_plan = models.CharField(max_length=100)
    cobertura_plan = models.CharField(max_length=100)
    condiciones = models.FloatField()

    class Meta():
        db_table = "planes"

    def __str__(self):
        return self.nombre_plan


tipos = [
    ('DNI', 'DNI'),
    ('PASAPORTE''', 'Pasaporte'),
    ('CI', 'Cedula de Extranjeria')
]

opciones_preguntas = [
    (1, 'Si'),
    (0, 'No')
]


class Planilla(models.Model):
    aseguradora = models.CharField(max_length=100)
    poliza = models.CharField(max_length=30)
    plan1 = models.BooleanField(default=False)
    plan2 = models.BooleanField(default=False)
    plan3 = models.BooleanField(default=False)
    legajo = models.CharField(max_length=30)
    titular = models.CharField(max_length=50)
    documento = models.CharField(max_length=20)
    tipodoc = models.CharField(max_length=20, choices=tipos)
    fechanacimiento = models.DateField()
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()
    montoasegurado = models.FloatField()
    fechainicio = models.DateField()
    cobertura1 = models.BooleanField(default=False)
    cobertura2 = models.BooleanField(default=False)
    cobertura3 = models.BooleanField(default=False)
    beneficiarios = models.CharField(max_length=3, blank=True)
    pregunta1 = models.BooleanField(
        default=False, choices=opciones_preguntas)
    pregunta2 = models.BooleanField(
        default=False, choices=opciones_preguntas)
    pregunta3 = models.BooleanField(
        default=False, choices=opciones_preguntas)

    class Meta():
        db_table = "planilla"

    def __str__(self):
        return self.titular


class Clientes(models.Model):
    titular = models.CharField(max_length=50)
    documento = models.CharField(max_length=20)
    tipodoc = models.CharField(max_length=20, choices=tipos)
    fechanacimiento = models.DateField()
    edad = models.IntegerField()
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    class Meta():
        db_table = "clientes"

    def __str__(self):
        return self.titular
