# Generated by Django 5.1 on 2024-09-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_fee_parent_alter_fee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='fee',
            name='small_desc',
            field=models.TextField(null=True),
        ),
    ]
