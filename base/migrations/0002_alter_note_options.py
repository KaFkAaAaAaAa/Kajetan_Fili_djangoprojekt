# Generated by Django 5.0.6 on 2024-05-24 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ('-publish', 'priority')},
        ),
    ]
