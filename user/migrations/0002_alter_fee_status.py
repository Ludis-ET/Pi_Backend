# Generated by Django 5.1 on 2024-09-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='status',
            field=models.CharField(choices=[('Paid', 'PAID'), ('UNPAID', 'Unpaid')], max_length=7),
        ),
    ]
