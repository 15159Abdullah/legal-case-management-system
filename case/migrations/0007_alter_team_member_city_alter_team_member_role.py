# Generated by Django 4.1.2 on 2023-02-25 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0006_team_member_zip_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team_member',
            name='city',
            field=models.CharField(choices=[('peshawar', 'Peshawar'), ('islamabad', 'Islamabad'), ('lahore', 'Lahore')], max_length=10),
        ),
        migrations.AlterField(
            model_name='team_member',
            name='role',
            field=models.CharField(choices=[('Admin', 'Administratore'), ('Data Entry', 'Data Entry')], max_length=11),
        ),
    ]
