# Generated by Django 3.1.7 on 2021-03-21 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
        ('artworks', '0003_auto_20210320_1623'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artworks',
            name='artist_id',
        ),
        migrations.AddField(
            model_name='artworks',
            name='artist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='members.members'),
        ),
    ]