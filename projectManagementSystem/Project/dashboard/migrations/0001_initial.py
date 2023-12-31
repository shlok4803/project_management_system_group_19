# Generated by Django 4.2.5 on 2023-11-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('projectID', models.SlugField(max_length=15, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('completed', models.DateTimeField(blank=True)),
                ('status', models.CharField(choices=[('O', 'Ongoing'), ('C', 'Completed')], default='O', max_length=1)),
                ('ManagerName', models.CharField(blank=True, max_length=30)),
                ('ManagerEmail', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('taskID', models.SlugField(editable=False, max_length=32, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField(blank=True)),
                ('submitted', models.DateTimeField(blank=True)),
                ('completed', models.DateTimeField(blank=True)),
                ('assigned', models.DateTimeField()),
                ('EmployeeName', models.CharField(blank=True, max_length=30)),
                ('EmployeeEmail', models.EmailField(max_length=254, unique=True)),
                ('projectID', models.SlugField(max_length=15)),
                ('ManagerName', models.CharField(blank=True, max_length=30)),
                ('ManagerEmail', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(choices=[('I', 'In Progress'), ('C', 'Completed'), ('R', 'Submitted For Review')], default='N', max_length=1)),
            ],
        ),
    ]
