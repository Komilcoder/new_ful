# Generated by Django 2.2.5 on 2020-10-13 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smm_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=150)),
                ('familya', models.CharField(max_length=150)),
                ('telefon_raqam', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
            ],
        ),
    ]
