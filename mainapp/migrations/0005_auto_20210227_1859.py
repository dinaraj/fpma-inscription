# Generated by Django 3.1.7 on 2021-02-27 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210227_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='Numéro de téléphone'),
        ),
    ]