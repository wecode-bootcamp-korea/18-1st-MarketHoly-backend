# Generated by Django 3.1.7 on 2021-03-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccumulatedMoneyReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('money', models.IntegerField(null=True)),
                ('accumulated_rate', models.DecimalField(decimal_places=5, max_digits=8, null=True)),
            ],
            options={
                'db_table': 'accumulated_money_reason',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=45, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField(null=True)),
                ('saved_item', models.ManyToManyField(through='order.SavedItem', to='product.Product')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('detail_address', models.CharField(max_length=100, null=True)),
                ('is_default', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='AccumulatedMoneyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.accumulatedmoneyreason')),
            ],
            options={
                'db_table': 'accumulated_money_type',
            },
        ),
        migrations.CreateModel(
            name='AccumulatedMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accumulated_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('is_used', models.BooleanField(default=False)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.accumulatedmoneytype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'accumulated_money',
            },
        ),
    ]
