# Generated by Django 2.2.4 on 2019-08-24 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfuanime', '0002_auto_20190824_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='post_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
