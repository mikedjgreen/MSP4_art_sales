# Generated by Django 3.1.7 on 2021-03-18 17:05

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='original_basket',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='orders',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='orders',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]