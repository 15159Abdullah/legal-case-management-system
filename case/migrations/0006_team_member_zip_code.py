# Generated by Django 4.1.2 on 2023-02-25 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0005_delete_add_team_member'),
    ]

    operations = [
        migrations.AddField(
            model_name='team_member',
            name='zip_code',
            field=models.CharField(blank=True, max_length=7),
        ),
    ]