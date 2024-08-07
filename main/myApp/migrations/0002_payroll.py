# Generated by Django 5.0.7 on 2024-07-23 20:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('gross_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_deductions', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_bonuses', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_fringe_benefits', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('processed_date', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.employee')),
            ],
        ),
    ]
