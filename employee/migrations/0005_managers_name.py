# Generated by Django 4.0.3 on 2022-03-23 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_mgr'),
    ]

    operations = [
        migrations.AddField(
            model_name='managers',
            name='name',
            field=models.CharField(default='none', max_length=100),
            preserve_default=False,
        ),
    ]
