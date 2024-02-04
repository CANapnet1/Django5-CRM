# Generated by Django 5.0.1 on 2024-02-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(max_length=10, null=True)),
                ('client_firstname', models.CharField(max_length=100, null=True)),
                ('client_lasttname', models.CharField(max_length=100, null=True)),
                ('client_date', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('client_id', models.CharField(max_length=10, null=True)),
                ('client_genre', models.CharField(max_length=50, null=True)),
                ('client_rating', models.IntegerField(null=True)),
            ],
        ),
    ]