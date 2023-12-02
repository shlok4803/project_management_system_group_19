# Generated by Django 4.2.5 on 2023-11-07 10:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_project_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ownerEmail',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='ownerName',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
