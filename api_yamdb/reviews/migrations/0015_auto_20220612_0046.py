# Generated by Django 2.2.16 on 2022-06-11 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20220612_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ('name',)},
        ),
    ]