# Generated by Django 3.1.4 on 2020-12-24 07:44

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20201224_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='conte', unique=True),
        ),
    ]
