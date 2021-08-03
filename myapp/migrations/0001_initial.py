# Generated by Django 3.2.5 on 2021-07-16 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('text', models.CharField(max_length=140, verbose_name='Fleet')),
                ('date', models.DateTimeField(default=True)),
            ],
        ),
    ]
