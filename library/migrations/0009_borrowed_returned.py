# Generated by Django 2.1.7 on 2019-11-25 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='returned',
            field=models.IntegerField(default=-1),
        ),
    ]