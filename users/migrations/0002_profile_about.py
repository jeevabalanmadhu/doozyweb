# Generated by Django 4.0.6 on 2022-07-24 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default='n'),
            preserve_default=False,
        ),
    ]
