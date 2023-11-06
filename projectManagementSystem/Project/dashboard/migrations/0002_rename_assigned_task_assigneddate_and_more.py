# Generated by Django 4.2.5 on 2023-11-04 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigned',
            new_name='assignedDate',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='taskName',
        ),
        migrations.RemoveField(
            model_name='task',
            name='ManagerName',
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='projectID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.project'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('I', 'In Progress'), ('C', 'Completed'), ('R', 'Submitted For Review')], default='I', max_length=1),
        ),
    ]
