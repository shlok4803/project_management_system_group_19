# Generated by Django 4.2.5 on 2023-10-02 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'Employee-User', 'verbose_name_plural': 'Employee-Users'},
        ),
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Manager-User', 'verbose_name_plural': 'Manager-Users'},
        ),
        migrations.AlterModelOptions(
            name='owner',
            options={'verbose_name': 'Owner-User', 'verbose_name_plural': 'Owner-Users'},
        ),
    ]