# Generated by Django 3.2.7 on 2021-09-13 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('document_type', models.CharField(choices=[('V', 'Venezolano'), ('E', 'Extranjero')], max_length=1)),
                ('document_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.TextField(max_length=500)),
                ('state', models.CharField(default='A', max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Client',
            },
        ),
        migrations.CreateModel(
            name='ForeignTransfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_abroad', models.CharField(max_length=1)),
                ('origin', models.CharField(blank=True, choices=[('Ven', 'Venezuela'), ('Col', 'Colombia'), ('Per', 'Peru'), ('Chi', 'Chile'), ('Bra', 'Brasil'), ('Arg', 'Argentina'), ('Ecu', 'Ecuador')], max_length=3, null=True)),
                ('destiny', models.CharField(blank=True, choices=[('Ven', 'Venezuela'), ('Col', 'Colombia'), ('Per', 'Peru'), ('Chi', 'Chile'), ('Bra', 'Brasil'), ('Arg', 'Argentina'), ('Ecu', 'Ecuador')], max_length=3, null=True)),
            ],
            options={
                'db_table': 'ForeignTransfer',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('state', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'Municipality',
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('address', models.TextField(max_length=500)),
                ('state', models.CharField(default='A', max_length=1)),
                ('municipality_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_cuentas.municipality')),
            ],
            options={
                'db_table': 'Office',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('state', models.CharField(default='A', max_length=1)),
            ],
            options={
                'db_table': 'State',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('account_type', models.CharField(choices=[('CA', 'Cuenta de ahorro'), ('CC', 'Cuenta corriente')], max_length=2)),
                ('reason', models.CharField(choices=[('BS', 'Buen servicio y variedad de productos'), ('CT', 'Cliente tradicional'), ('CN', 'Cuenta Nomina'), ('GFB', 'Gestion de Funcionario del banco'), ('NN', 'Por estar a nivel nacional'), ('SPS', 'Por la solidez / prestigio / seguridad'), ('AI', 'Por los altos intereses'), ('PRE', 'Por los premios'), ('PUB', 'Publicidad'), ('RFA', 'Referencia de un familiar / amigo')], max_length=3)),
                ('expiration_date', models.DateField()),
                ('date_issue', models.DateField(auto_now_add=True)),
                ('account_usage', models.CharField(choices=[('APE', 'Ahorro personal'), ('AGVP', 'Atender gastos varios / personales'), ('CCC', 'Cancelar cuotas de credito'), ('DV', 'Deposito de las ventas'), ('MFNPF', 'Movilizar fondos de nomina / pension / fideicomiso'), ('PP', 'Pago de proveedores'), ('P', 'Particular'), ('RDA', 'Recibir deposito de alquileres'), ('RIDP', 'Recibir intereses de depositos a plazo')], max_length=5)),
                ('estimated_amount_mobilization', models.CharField(choices=[('En0y500', 'Entre 0 y 500'), ('En100001y100000', 'Entre 10.001 y 100.000'), ('En2501y10000', 'Entre 2.501 y 10.000'), ('En501y2500', 'Entre 501 y 2.500'), ('Ma100001', 'Mas de 100.001')], max_length=15)),
                ('average_monthly_transaction', models.CharField(choices=[('Ma100', 'Mayor que 100'), ('Me20', 'Menor que 20'), ('Ma20Me50', 'Mayor que 20 y menor que 50'), ('Ma51Me100', 'Mayor que 51 y menor que 100')], max_length=9)),
                ('background_source', models.CharField(max_length=1)),
                ('background_destination', models.CharField(max_length=1)),
                ('state', models.CharField(default='A', max_length=1)),
                ('client_document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_cuentas.client')),
                ('foreign_transfer_code', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pre_cuentas.foreigntransfer')),
                ('office_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_cuentas.office')),
            ],
            options={
                'db_table': 'Request',
            },
        ),
        migrations.AddField(
            model_name='municipality',
            name='state_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_cuentas.state'),
        ),
        migrations.AddConstraint(
            model_name='client',
            constraint=models.UniqueConstraint(fields=('document_type', 'document_number'), name='unique_document'),
        ),
    ]
