# Generated by Django 3.1.7 on 2021-03-15 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bupehandler', '0021_auto_20210315_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites_all',
            name='samhsa_ftloc_id',
            field=models.ManyToManyField(blank=True, null=True, to='bupehandler.Siterecs_samhsa_ftloc'),
        ),
    ]
