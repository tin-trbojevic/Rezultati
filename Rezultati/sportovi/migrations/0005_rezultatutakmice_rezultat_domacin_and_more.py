# Generated by Django 4.2.10 on 2024-02-16 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sportovi', '0004_remove_rezultatutakmice_rezultat_domacin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rezultatutakmice',
            name='rezultat_domacin',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rezultatutakmice',
            name='rezultat_gost',
            field=models.IntegerField(default=0),
        ),
    ]
