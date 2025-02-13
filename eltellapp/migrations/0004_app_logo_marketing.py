# Generated by Django 5.0.2 on 2024-04-03 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eltellapp', '0003_rename_rate_worker_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=254, upload_to=None)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=254, upload_to=None)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Marketing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=254, upload_to=None)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]
