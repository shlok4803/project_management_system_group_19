# Generated by Django 4.2.5 on 2023-11-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_customuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='company_name',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
