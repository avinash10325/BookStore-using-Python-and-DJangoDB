# Generated by Django 3.1.3 on 2020-11-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='stock',
            field=models.IntegerField(default=5),
        ),
    ]
