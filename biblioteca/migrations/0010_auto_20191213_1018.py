# Generated by Django 2.2.8 on 2019-12-13 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0009_auto_20191212_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='generos',
            field=models.ManyToManyField(help_text='Select a genre for this book', null=True, to='biblioteca.Genero'),
        ),
    ]