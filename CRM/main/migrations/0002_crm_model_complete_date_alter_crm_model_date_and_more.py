# Generated by Django 5.1.7 on 2025-03-31 14:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm_model',
            name='complete_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='crm_model',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='crm_model',
            name='type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
