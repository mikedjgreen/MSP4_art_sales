# Generated by Django 3.1.7 on 2021-03-25 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='members',
            name='admin_id',
        ),
        migrations.AddField(
            model_name='members',
            name='username',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='members',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]
