# Generated by Django 3.1.7 on 2021-03-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_auto_20210227_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Contenu additionnel'),
        ),
        migrations.AddField(
            model_name='event',
            name='email_alert',
            field=models.EmailField(default='d.rajaonson@gmail.com', max_length=250, verbose_name='Adresse mail qui reçoit les alertes'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='email_footer',
            field=models.TextField(blank=True, null=True, verbose_name='Texte dans le footer du mail'),
        ),
        migrations.AddField(
            model_name='event',
            name='email_from',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Expéditeur email. Ex: FPMA Réunion<fpmareunion@gmail.com>'),
        ),
        migrations.AddField(
            model_name='event',
            name='paroisse',
            field=models.CharField(default='Réunion', max_length=250, verbose_name='Paroisse'),
            preserve_default=False,
        ),
    ]