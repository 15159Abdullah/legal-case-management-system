# Generated by Django 4.1.2 on 2023-02-26 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0020_alter_appiontment_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appiontment',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
