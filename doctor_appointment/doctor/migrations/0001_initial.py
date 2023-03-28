# Generated by Django 4.1.7 on 2023-02-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='doctor_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('doctor_id', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now=True, null=True)),
                ('time', models.TimeField(auto_now=True, null=True)),
                ('status', models.CharField(default=True, max_length=250)),
            ],
        ),
    ]
