# Generated by Django 4.2 on 2023-04-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aplicaciones', '0003_remove_usuario_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciudad', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateField()),
                ('hora', models.TimeField()),
                ('comentarios', models.CharField(max_length=50)),
            ],
        ),
    ]
