# Generated by Django 3.1.7 on 2021-03-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_subs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]
