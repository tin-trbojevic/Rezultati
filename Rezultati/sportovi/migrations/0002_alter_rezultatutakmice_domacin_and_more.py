# Generated by Django 4.2.10 on 2024-02-16 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sportovi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezultatutakmice',
            name='domacin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domacin_utakmice', to='sportovi.tim'),
        ),
        migrations.AlterField(
            model_name='rezultatutakmice',
            name='gost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gost_utakmice', to='sportovi.tim'),
        ),
    ]
