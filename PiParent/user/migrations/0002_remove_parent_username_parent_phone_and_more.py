# Generated by Django 5.0.1 on 2024-08-31 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parent',
            name='username',
        ),
        migrations.AddField(
            model_name='parent',
            name='phone',
            field=models.CharField(default=0, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parent',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
