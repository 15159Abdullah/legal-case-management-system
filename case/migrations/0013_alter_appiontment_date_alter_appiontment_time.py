# Generated by Django 4.1.2 on 2023-02-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0012_alter_appiontment_date_alter_appiontment_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiontment',
            name='date',
            field=models.DateField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='appiontment',
            name='time',
            field=models.TimeField(blank=True, max_length=20, null=True),
        ),
    ]