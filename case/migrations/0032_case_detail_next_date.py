# Generated by Django 4.1.2 on 2023-02-27 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0031_case_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_detail',
            name='next_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
