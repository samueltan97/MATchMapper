# Generated by Django 3.1.7 on 2021-03-09 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bupehandler', '0014_auto_20210309_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sites_all',
            name='other_srcs_id',
        ),
        migrations.AddField(
            model_name='sites_all',
            name='other_srcs_id',
            field=models.ManyToManyField(to='bupehandler.Siterecs_other_srcs'),
        ),
        migrations.CreateModel(
            name='sitesrecs_other_srcs_sitesall_lk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_srcs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bupehandler.sites_all')),
                ('site_id_samhsa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bupehandler.siterecs_other_srcs')),
            ],
        ),
        migrations.AddField(
            model_name='siterecs_other_srcs',
            name='site_id',
            field=models.ManyToManyField(through='bupehandler.sitesrecs_other_srcs_sitesall_lk', to='bupehandler.Sites_all'),
        ),
    ]