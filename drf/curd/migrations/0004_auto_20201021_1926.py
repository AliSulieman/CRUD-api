# Generated by Django 3.1.2 on 2020-10-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curd', '0003_user_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.TextField(),
        ),
    ]
