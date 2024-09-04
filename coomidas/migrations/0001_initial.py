# Generated by Django 5.0.7 on 2024-09-04 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=25)),
                ('nombre_receta', models.CharField(max_length=40)),
                ('puntaje', models.FloatField()),
                ('comentario', models.CharField(max_length=450)),
                ('fecha_comentario', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recetas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('ingredientes', models.TextField()),
                ('preparacion', models.CharField(max_length=2600)),
                ('dificultad', models.IntegerField()),
                ('resumen_de_la_receta', models.CharField(max_length=1000)),
                ('username', models.CharField(max_length=20)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
            ],
        ),
    ]
