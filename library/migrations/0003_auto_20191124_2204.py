# Generated by Django 2.1.7 on 2019-11-24 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20191124_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sub_category',
            name='deleted_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]