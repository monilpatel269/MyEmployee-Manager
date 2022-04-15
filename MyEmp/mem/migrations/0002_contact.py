# Generated by Django 4.0.3 on 2022-04-13 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(default='', max_length=30)),
                ('phone', models.IntegerField(default='')),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
    ]
