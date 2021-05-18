# Generated by Django 3.2.3 on 2021-05-16 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=120)),
                ('direccion', models.CharField(max_length=150)),
                ('correo', models.EmailField(max_length=100)),
            ],
        ),
    ]