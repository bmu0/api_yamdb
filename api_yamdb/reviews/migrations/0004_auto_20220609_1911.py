# Generated by Django 2.2.16 on 2022-06-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220609_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=6, verbose_name='confirmation code'),
        ),
    ]
