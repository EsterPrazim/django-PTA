from django.db import models
from solo.models import SingletonModel

# Create your models here.
class Servico(models.Model):
    title = models.CharField('Título', max_length=50)
    text = models.TextField('Texto', null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')

    class Meta:
        ordering = ['title']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.title

class Depoimento(models.Model):
    name = models.CharField('Nome',max_length=60)
    url = models.URLField('Link', max_length=300)
    image = models.ImageField(upload_to='depoimentos/', verbose_name='Imagem', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Depoimento'
        verbose_name_plural = 'Depoimentos'

    def __str__(self):
        return self.name

class QuemSomos(SingletonModel):
    aboutUs = models.TextField('Sobre nós', max_length=200)
    description = models.TextField('Descrição', max_length=400)

    class Meta:
        verbose_name = 'Quem somos'

    def __str__(self):
        return "Quem somos"