# Generated by Django 3.0.5 on 2020-04-13 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=128)),
                ('address_2', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=64)),
                ('zipcode', models.CharField(max_length=6)),
                ('num_adults', models.IntegerField()),
                ('num_children', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
