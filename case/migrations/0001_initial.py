# Generated by Django 4.1.2 on 2023-02-24 04:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='client_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('contact', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=50)),
                ('refname', models.CharField(max_length=50)),
                ('refcontact', models.CharField(blank=True, max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
    ]
