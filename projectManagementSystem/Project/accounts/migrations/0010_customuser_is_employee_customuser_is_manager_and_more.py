# Generated by Django 4.2.5 on 2023-11-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
    ]
