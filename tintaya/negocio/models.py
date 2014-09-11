from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class registrado(models.Model):
	nombre = models.CharField(max_length=200, null=True,blank=True)
	apellido = models.CharField(max_length=200, null=True,blank=True)
	email = models.EmailField()
	fechaCreacion = models.DateTimeField(auto_now_add=True,auto_now=False)
	fechaModificacion = models.DateTimeField(auto_now_add=False,auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.nombre,'',self.apellido)

