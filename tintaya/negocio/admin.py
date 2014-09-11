from django.contrib import admin

# Register your models here.
from .models import registrado


class AdminRegistrado(admin.ModelAdmin):
	class Meta:
		model = registrado


admin.site.register(registrado,AdminRegistrado)