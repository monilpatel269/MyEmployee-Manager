# Generated by Django 4.0.3 on 2022-04-13 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('location', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(default='', max_length=30)),
                ('salary', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('hiredate', models.DateField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mem.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mem.role')),
            ],
        ),
    ]
