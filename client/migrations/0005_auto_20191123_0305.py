# Generated by Django 2.1.7 on 2019-11-23 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_auto_20191123_0223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='client-register-dob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-first-name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-last-name',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-middle-name',
            new_name='middle_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='client-register-SUO',
            new_name='signed_up_on',
        ),
    ]
