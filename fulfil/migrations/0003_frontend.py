# Generated by Django 2.2.5 on 2020-10-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fulfil', '0002_smm_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Frontend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=150)),
                ('familya', models.CharField(max_length=150)),
                ('telefon_raqam', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
            ],
        ),
    ]
