# Generated by Django 4.2.7 on 2023-11-13 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0020_alter_task_completed_alter_task_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]