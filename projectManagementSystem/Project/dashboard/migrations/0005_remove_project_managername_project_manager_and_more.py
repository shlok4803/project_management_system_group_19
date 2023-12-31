# Generated by Django 4.2.5 on 2023-11-06 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_rename_title_project_projecttitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='ManagerName',
        ),
        migrations.AddField(
            model_name='project',
            name='manager',
            field=models.ForeignKey(null='True', on_delete=django.db.models.deletion.CASCADE, related_name='projects_managed', to=settings.AUTH_USER_MODEL),
            preserve_default='True',
        ),
        migrations.AlterField(
            model_name='project',
            name='completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
