# Generated by Django 3.1.7 on 2021-02-27 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210227_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='list_names',
            field=models.TextField(blank=True, null=True, verbose_name='Prénom des personnes'),
        ),
    ]