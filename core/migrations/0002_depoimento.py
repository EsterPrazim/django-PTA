# Generated by Django 2.2.7 on 2019-11-09 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depoimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Nome')),
                ('url', models.URLField(max_length=300, verbose_name='Link')),
                ('image', models.ImageField(upload_to='depoimentos/', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Depoimento',
                'verbose_name_plural': 'Depoimentos',
                'ordering': ['name'],
            },
        ),
    ]