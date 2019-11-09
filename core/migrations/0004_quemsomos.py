# Generated by Django 2.2.7 on 2019-11-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191109_0238'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aboutUs', models.TextField(max_length=200, verbose_name='Sobre nós')),
                ('description', models.TextField(max_length=400, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Quem somos',
            },
        ),
    ]
