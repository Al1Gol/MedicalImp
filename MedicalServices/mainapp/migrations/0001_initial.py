# Generated by Django 4.0.5 on 2022-07-04 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('address', models.CharField(max_length=1000)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.clients')),
            ],
            options={
                'unique_together': {('client_name', 'name')},
            },
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.BigIntegerField(default=None, verbose_name='№')),
                ('sum', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('service', models.CharField(max_length=1000)),
                ('fraud_score', models.FloatField()),
                ('service_class', models.IntegerField()),
                ('service_name', models.CharField(max_length=100)),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.clients')),
                ('client_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.organizations')),
            ],
            options={
                'unique_together': {('client_org', 'num')},
            },
        ),
    ]
