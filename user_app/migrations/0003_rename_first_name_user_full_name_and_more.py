# Generated by Django 5.1.3 on 2024-11-25 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_user_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='full_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
    ]