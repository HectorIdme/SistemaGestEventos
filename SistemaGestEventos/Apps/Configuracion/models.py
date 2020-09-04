from django.db import models


# Create your models here.
class Ambientes(models.Model):
    Nombre = models.CharField(max_length=50)
    Ubicacion = models.CharField(max_length=50)
    Capacidad = models.IntegerField()

    def __str__(self):
        return "{0} => {1}".format(self.Nombre, self.Capacidad)


class Actividades(models.Model):
    Descripcion = models.CharField(max_length=50)
    Ambientes = models.ForeignKey(Ambientes, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.Descripcion


class Materiales(models.Model):
    Item = models.CharField(max_length=15)
    Cantidad = models.IntegerField()
    Costo = models.FloatField()

    def __str__(self):
        return self.Item


class Evento(models.Model):
    Nombre = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
    Estado = models.BooleanField(default=True)
    Activ = models.ManyToManyField(Actividades)

    def __str__(self):
        return "{0} => {1}".format(self.Nombre, self.Tipo)


class Asistente(models.Model):
    ApellidoPaterno = models.CharField(max_length=15)
    ApellidoMaterno = models.CharField(max_length=15)
    Nombres = models.CharField(max_length=15)
    DNI = models.CharField(max_length=8)
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'), ('N', 'No especifica'))
    Sexo = models.CharField(max_length=1, choices=SEXOS, default='M')

    def nombre_completo(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.nombre_completo()


class Inscripcion(models.Model):
    Asistente = models.ForeignKey(Asistente, null=False, blank=False, on_delete=models.CASCADE)
    Evento = models.ForeignKey(Evento, null=False, blank=False, on_delete=models.CASCADE)
    Fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        cadena = "{0} => {1}"
        return cadena.format(self.Asistente, self.Evento.Nombre)
