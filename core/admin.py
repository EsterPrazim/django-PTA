from django.contrib import admin
from .models import Servico, Depoimento

# Register your models here.

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date')

admin.site.register(Servico, ServicoAdmin)
admin.site.register(Depoimento)
