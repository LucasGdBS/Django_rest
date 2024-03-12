# Generated by Django 5.0.3 on 2024-03-11 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_nickname', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=150)),
                ('user_email', models.CharField(default='', max_length=150)),
                ('user_age', models.IntegerField(default=0)),
            ],
        ),
    ]
