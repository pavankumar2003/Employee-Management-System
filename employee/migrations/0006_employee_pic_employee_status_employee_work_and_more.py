# Generated by Django 4.0.3 on 2022-04-27 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_managers_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='status',
            field=models.CharField(default='in progress', max_length=20),
        ),
        migrations.AddField(
            model_name='employee',
            name='work',
            field=models.TextField(default='No assigned work'),
        ),
        migrations.AddField(
            model_name='managers',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='managers',
            name='status',
            field=models.CharField(default='in progress', max_length=20),
        ),
        migrations.AddField(
            model_name='managers',
            name='task',
            field=models.TextField(default='No task'),
        ),
    ]
