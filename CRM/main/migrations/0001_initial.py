# Generated by Django 5.1.7 on 2025-03-30 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CRM_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=50, null=True)),
                ('date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('product_description', models.TextField(default='Описания нет', max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('contacts', models.CharField(max_length=60)),
                ('quality', models.CharField(choices=[('C', 'Normal'), ('B', 'Good'), ('A', 'Medium'), ('S', 'Premium'), ('SS', 'Elite')], default='A', max_length=15)),
                ('type', models.CharField(max_length=15, null=True)),
                ('checkbox', models.BooleanField(default=False)),
            ],
        ),
    ]
