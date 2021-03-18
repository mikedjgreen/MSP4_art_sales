# Generated by Django 3.1.7 on 2021-03-18 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('checkout', '0002_auto_20210318_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='user_id',
        ),
        migrations.AddField(
            model_name='orders',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.patron'),
        ),
    ]
