# Generated by Django 3.1.7 on 2021-03-26 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artworks', '0004_auto_20210321_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artworks',
            name='depth',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]