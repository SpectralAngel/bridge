# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, null=True, blank=True)),
                ('loan', models.IntegerField()),
            ],
            options={
                'db_table': 'account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('card_id', models.CharField(max_length=15, null=True, blank=True)),
                ('gender', models.CharField(max_length=1, null=True, blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('birth_place', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('phone', models.TextField(null=True, blank=True)),
                ('state', models.CharField(max_length=50, null=True, blank=True)),
                ('school', models.CharField(max_length=255, null=True, blank=True)),
                ('town', models.CharField(max_length=50, null=True, blank=True)),
                ('joined', models.DateField(null=True, blank=True)),
                ('active', models.IntegerField(null=True, blank=True)),
                ('escalafon', models.CharField(max_length=11, null=True, blank=True)),
                ('inprema', models.CharField(max_length=11, null=True, blank=True)),
                ('payment', models.CharField(max_length=20)),
                ('jubilated', models.DateField(null=True, blank=True)),
                ('reason', models.CharField(max_length=50, null=True, blank=True)),
                ('desactivacion', models.DateField(null=True, blank=True)),
                ('muerte', models.DateField(null=True, blank=True)),
                ('banco', models.IntegerField(null=True, blank=True)),
                ('cuenta', models.CharField(max_length=20, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('instituto_id', models.IntegerField(null=True, blank=True)),
                ('banco_completo', models.IntegerField()),
                ('bancario', models.CharField(max_length=255, null=True, blank=True)),
                ('last', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'affiliate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alquiler',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField()),
                ('descripcion', models.CharField(max_length=255, null=True, blank=True)),
                ('inquilino', models.CharField(max_length=100, null=True, blank=True)),
                ('monto', models.DecimalField(max_digits=10, decimal_places=0)),
                ('mora', models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)),
                ('impuesto', models.DecimalField(null=True, max_digits=10, decimal_places=0, blank=True)),
            ],
            options={
                'db_table': 'alquiler',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Asamblea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.IntegerField(null=True, blank=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('habilitado', models.IntegerField()),
                ('fecha', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'asamblea',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'autorizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AutoSeguro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('month1', models.IntegerField(null=True, blank=True)),
                ('month2', models.IntegerField(null=True, blank=True)),
                ('month3', models.IntegerField(null=True, blank=True)),
                ('month4', models.IntegerField(null=True, blank=True)),
                ('month5', models.IntegerField(null=True, blank=True)),
                ('month6', models.IntegerField(null=True, blank=True)),
                ('month7', models.IntegerField(null=True, blank=True)),
                ('month8', models.IntegerField(null=True, blank=True)),
                ('month9', models.IntegerField(null=True, blank=True)),
                ('month10', models.IntegerField(null=True, blank=True)),
                ('month11', models.IntegerField(null=True, blank=True)),
                ('month12', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'auto_seguro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Auxilio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cobrador', models.CharField(max_length=100, null=True, blank=True)),
                ('fecha', models.DateTimeField()),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cheque', models.CharField(max_length=20, null=True, blank=True)),
                ('banco', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'auxilio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AyudaFunebre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cheque', models.CharField(max_length=20, null=True, blank=True)),
                ('pariente', models.CharField(max_length=100, null=True, blank=True)),
                ('banco', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'ayuda_funebre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Banco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('depositable', models.IntegerField()),
                ('asambleista', models.IntegerField()),
                ('parser', models.CharField(max_length=45)),
                ('generator', models.CharField(max_length=45)),
                ('codigo', models.CharField(max_length=45, null=True, blank=True)),
                ('cuenta', models.CharField(max_length=45, null=True, blank=True)),
                ('cuota', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'banco',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'bank_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BankReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('month', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'bank_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Beneficiario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cheque', models.CharField(max_length=20)),
                ('banco', models.CharField(max_length=50, null=True, blank=True)),
                ('fecha', models.DateTimeField()),
            ],
            options={
                'db_table': 'beneficiario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=100, null=True, blank=True)),
                ('telefono', models.CharField(max_length=11, null=True, blank=True)),
                ('activa', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'casa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CobroBancarioBanhcafe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identidad', models.CharField(max_length=13, null=True, blank=True)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('consumido', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cobro_bancario_banhcafe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cotizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
                ('jubilados', models.IntegerField()),
                ('bank_main', models.IntegerField()),
                ('alternate', models.IntegerField()),
                ('normal', models.IntegerField()),
                ('ordering', models.CharField(max_length=45, null=True, blank=True)),
            ],
            options={
                'db_table': 'cotizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CotizacionTgUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cotizacion_id', models.IntegerField()),
                ('tg_user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'cotizacion_tg_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cubiculo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, null=True, blank=True)),
                ('inquilino', models.CharField(max_length=255, null=True, blank=True)),
                ('precio', models.DecimalField(max_digits=10, decimal_places=0)),
                ('enee', models.CharField(max_length=100)),
                ('interes', models.DecimalField(max_digits=10, decimal_places=0)),
            ],
            options={
                'db_table': 'cubiculo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CuentaRetrasada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(null=True, blank=True)),
                ('anio', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'cuenta_retrasada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CuotaTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField()),
                ('month1', models.IntegerField()),
                ('month2', models.IntegerField()),
                ('month3', models.IntegerField()),
                ('month4', models.IntegerField()),
                ('month5', models.IntegerField()),
                ('month6', models.IntegerField()),
                ('month7', models.IntegerField()),
                ('month8', models.IntegerField()),
                ('month9', models.IntegerField()),
                ('month10', models.IntegerField()),
                ('month11', models.IntegerField()),
                ('month12', models.IntegerField()),
            ],
            options={
                'db_table': 'cuota_table',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DeduccionBancaria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('detail', models.TextField(null=True, blank=True)),
                ('day', models.DateField(null=True, blank=True)),
                ('month', models.IntegerField(null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'deduccion_bancaria',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deduced',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('detail', models.CharField(max_length=150, null=True, blank=True)),
                ('cotizacion_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'deduced',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'deduction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=60, null=True, blank=True)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepartamentoTgUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departamento_id', models.IntegerField()),
                ('tg_user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'departamento_tg_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Deposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliado_id', models.IntegerField(null=True, blank=True)),
                ('banco_id', models.IntegerField(null=True, blank=True)),
                ('concepto', models.CharField(max_length=50, null=True, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('posteo', models.DateField(null=True, blank=True)),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'deposito',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DepositoAnonimo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referencia', models.CharField(max_length=100, null=True, blank=True)),
                ('banco_id', models.IntegerField(null=True, blank=True)),
                ('concepto', models.CharField(max_length=50, null=True, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'deposito_anonimo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleBancario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'detalle_bancario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, null=True, blank=True)),
                ('valor', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'detalle_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Devolucion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('concepto', models.CharField(max_length=200, null=True, blank=True)),
                ('fecha', models.DateTimeField()),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cheque', models.CharField(max_length=20, null=True, blank=True)),
                ('banco', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'devolucion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'distribution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('months', models.IntegerField(null=True, blank=True)),
                ('retrasada', models.IntegerField(null=True, blank=True)),
                ('mes', models.IntegerField(null=True, blank=True)),
                ('anio', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'extra',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instituto', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'filial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=15, null=True, blank=True)),
            ],
            options={
                'db_table': 'forma_pago',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'group_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Indemnizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'indemnizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliado_id', models.IntegerField(null=True, blank=True)),
                ('asamblea_id', models.IntegerField(null=True, blank=True)),
                ('viatico_id', models.IntegerField(null=True, blank=True)),
                ('enviado', models.IntegerField(null=True, blank=True)),
                ('envio', models.DateField(null=True, blank=True)),
                ('ingresado', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'inscripcion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Instituto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'instituto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capital', models.DecimalField(max_digits=10, decimal_places=2)),
                ('letters', models.TextField(null=True, blank=True)),
                ('debt', models.DecimalField(max_digits=10, decimal_places=2)),
                ('payment', models.DecimalField(max_digits=10, decimal_places=2)),
                ('interest', models.DecimalField(max_digits=4, decimal_places=2)),
                ('months', models.IntegerField(null=True, blank=True)),
                ('last', models.DateField(null=True, blank=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('start_date', models.DateField()),
                ('aproved', models.IntegerField(null=True, blank=True)),
                ('offset', models.IntegerField(null=True, blank=True)),
                ('fecha_mora', models.DateField()),
                ('cobrar', models.IntegerField(null=True, blank=True)),
                ('acumulado', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('vence', models.DateField(null=True, blank=True)),
                ('vencidas', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'loan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.TextField(null=True, blank=True)),
                ('day', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'logger',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Obligation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('inprema', models.DecimalField(max_digits=10, decimal_places=2)),
                ('filiales', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('inprema_compliment', models.DecimalField(max_digits=10, decimal_places=2)),
                ('amount_compliment', models.DecimalField(max_digits=10, decimal_places=2)),
                ('alternate', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'obligation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Observacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('texto', models.TextField(null=True, blank=True)),
                ('fecha', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'observacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OldPay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('capital', models.DecimalField(max_digits=10, decimal_places=2)),
                ('interest', models.DecimalField(max_digits=10, decimal_places=2)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('receipt', models.TextField(null=True, blank=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'old_pay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'organizacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OtherAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'other_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OtherReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('month', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'other_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagoBancarioBanhcafe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identidad', models.CharField(max_length=13, null=True, blank=True)),
                ('cantidad', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('fecha', models.DateTimeField(null=True, blank=True)),
                ('referencia', models.IntegerField(null=True, blank=True)),
                ('agencia', models.IntegerField(null=True, blank=True)),
                ('cajero', models.CharField(max_length=10, null=True, blank=True)),
                ('terminal', models.CharField(max_length=10, null=True, blank=True)),
                ('aplicado', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'pago_bancario_banhcafe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagoFilial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField()),
                ('detalle', models.CharField(max_length=255, null=True, blank=True)),
                ('cheque', models.CharField(max_length=255, null=True, blank=True)),
                ('valor', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('saldo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'pago_filial',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField(null=True, blank=True)),
                ('capital', models.DecimalField(max_digits=10, decimal_places=2)),
                ('interest', models.DecimalField(max_digits=10, decimal_places=2)),
                ('amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('receipt', models.CharField(max_length=100, null=True, blank=True)),
                ('deposito', models.IntegerField()),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'db_table': 'pay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayedDeduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'payed_deduction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PayedLoan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('capital', models.DecimalField(max_digits=10, decimal_places=2)),
                ('letters', models.TextField(null=True, blank=True)),
                ('payment', models.DecimalField(max_digits=10, decimal_places=2)),
                ('interest', models.DecimalField(max_digits=4, decimal_places=2)),
                ('months', models.IntegerField()),
                ('last', models.DateField(null=True, blank=True)),
                ('start_date', models.DateField()),
                ('debt', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'payed_loan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission_name', models.CharField(unique=True, max_length=16)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PostReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('month', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'post_report',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('activo', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rechazo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reason', models.TextField(null=True, blank=True)),
                ('day', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'rechazo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliado', models.IntegerField(null=True, blank=True)),
                ('cliente', models.CharField(max_length=100)),
                ('dia', models.DateTimeField()),
                ('impreso', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recibo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReciboCeiba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliado', models.IntegerField(null=True, blank=True)),
                ('cliente', models.CharField(max_length=100)),
                ('dia', models.DateTimeField()),
                ('impreso', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recibo_ceiba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReciboDanli',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliado', models.IntegerField(null=True, blank=True)),
                ('cliente', models.CharField(max_length=100)),
                ('dia', models.DateTimeField()),
                ('impreso', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recibo_danli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReciboSps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('afiliado', models.IntegerField(null=True, blank=True)),
                ('cliente', models.CharField(max_length=100)),
                ('dia', models.DateTimeField()),
                ('impreso', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recibo_sps',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReciboTga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('casa_id', models.IntegerField(null=True, blank=True)),
                ('afiliado', models.IntegerField(null=True, blank=True)),
                ('cliente', models.CharField(max_length=100)),
                ('dia', models.DateTimeField()),
                ('impreso', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'recibo_tga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reintegro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affiliate_id', models.IntegerField(null=True, blank=True)),
                ('emision', models.DateField(null=True, blank=True)),
                ('monto', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('cheque', models.CharField(max_length=10, null=True, blank=True)),
                ('planilla', models.CharField(max_length=10, null=True, blank=True)),
                ('motivo', models.CharField(max_length=100, null=True, blank=True)),
                ('forma_pago_id', models.IntegerField(null=True, blank=True)),
                ('pagado', models.IntegerField(null=True, blank=True)),
                ('cancelacion', models.DateField(null=True, blank=True)),
                ('cuenta_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'reintegro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReportAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('account_id', models.IntegerField(null=True, blank=True)),
                ('quantity', models.IntegerField(null=True, blank=True)),
                ('amount', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'report_account',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReporteBancario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField(null=True, blank=True)),
                ('month', models.IntegerField(null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'reporte_bancario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ReversionBancariaBanhcafe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(null=True, blank=True)),
                ('referencia', models.IntegerField(null=True, blank=True)),
                ('agencia', models.IntegerField(null=True, blank=True)),
                ('terminal', models.CharField(max_length=10, null=True, blank=True)),
                ('cajero', models.CharField(max_length=10, null=True, blank=True)),
            ],
            options={
                'db_table': 'reversion_bancaria_banhcafe',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seguro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('fallecimiento', models.DateTimeField()),
            ],
            options={
                'db_table': 'seguro',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sobrevivencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('cheque', models.CharField(max_length=20, null=True, blank=True)),
                ('banco', models.CharField(max_length=50, null=True, blank=True)),
            ],
            options={
                'db_table': 'sobrevivencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingreso', models.DateField(null=True, blank=True)),
                ('entrega', models.DateField(null=True, blank=True)),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('periodo', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'solicitud',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SqlobjectDbVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.TextField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'sqlobject_db_version',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TgGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(unique=True, max_length=16)),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tg_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TgPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permission_name', models.CharField(unique=True, max_length=16)),
                ('description', models.CharField(max_length=255, null=True, blank=True)),
                ('child_name', models.CharField(max_length=255, null=True, blank=True)),
                ('done_constructing', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tg_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TgUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(unique=True, max_length=16)),
                ('email_address', models.CharField(unique=True, max_length=255)),
                ('display_name', models.CharField(max_length=255, null=True, blank=True)),
                ('password', models.CharField(max_length=40, null=True, blank=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'tg_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'user_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=200, null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('unitario', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'venta',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaCeiba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('unitario', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'venta_ceiba',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaDanli',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('unitario', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'venta_danli',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaSps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('unitario', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
                'db_table': 'venta_sps',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VentaTga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recibo_id', models.IntegerField(null=True, blank=True)),
                ('producto_id', models.IntegerField(null=True, blank=True)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('cantidad', models.IntegerField()),
                ('unitario', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'venta_tga',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Viatico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('transporte', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('previo', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('posterior', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
                'db_table': 'viatico',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_key', models.CharField(unique=True, max_length=40)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('expiry', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'visit',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VisitIdentity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visit_key', models.CharField(unique=True, max_length=40)),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'visit_identity',
                'managed': False,
            },
        ),
    ]
