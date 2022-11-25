# Generated by Django 4.0.6 on 2022-08-27 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='inicioM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulos-99')),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to='inicio')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('fechamodificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='noticiasM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200, verbose_name='Titulos-99')),
                ('contenido', models.TextField()),
                ('imagen', models.ImageField(upload_to='noticias')),
                ('fechacreacion', models.DateTimeField(auto_now_add=True)),
                ('fechamodificacion', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
