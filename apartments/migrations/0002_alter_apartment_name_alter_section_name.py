# Generated by Django 4.2.15 on 2024-08-26 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='name',
            field=models.TextField(max_length=100, verbose_name='Название квартиры'),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.TextField(max_length=100, verbose_name='Название секции'),
        ),
    ]
