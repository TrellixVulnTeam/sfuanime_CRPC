# Generated by Django 2.2.4 on 2019-08-24 20:17

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('sfuanime', '0004_auto_20190824_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
