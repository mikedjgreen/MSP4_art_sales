# Generated by Django 3.1.7 on 2021-03-29 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20210325_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(default=2021)),
                ('username', models.CharField(max_length=254)),
                ('paid', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_paid', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Subs',
            },
        ),
    ]