# Generated by Django 3.2.7 on 2021-09-19 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pre_cuentas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='background_destination',
        ),
        migrations.RemoveField(
            model_name='request',
            name='background_source',
        ),
        migrations.RemoveField(
            model_name='request',
            name='foreign_transfer_code',
        ),
        migrations.AddField(
            model_name='office',
            name='request_limit_day',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='request',
            name='transfer_destiny',
            field=models.CharField(choices=[('Ven', 'Venezuela'), ('Col', 'Colombia'), ('Per', 'Peru'), ('Chi', 'Chile'), ('Bra', 'Brasil'), ('Arg', 'Argentina'), ('Ecu', 'Ecuador')], default='Ven', max_length=3),
        ),
        migrations.AddField(
            model_name='request',
            name='transfer_origin',
            field=models.CharField(choices=[('Ven', 'Venezuela'), ('Col', 'Colombia'), ('Per', 'Peru'), ('Chi', 'Chile'), ('Bra', 'Brasil'), ('Arg', 'Argentina'), ('Ecu', 'Ecuador')], default='Ven', max_length=3),
        ),
        migrations.DeleteModel(
            name='ForeignTransfer',
        ),
    ]
