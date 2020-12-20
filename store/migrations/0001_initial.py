# Generated by Django 3.1.3 on 2020-11-27 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('Book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=70)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]