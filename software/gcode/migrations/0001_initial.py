# Generated by Django 5.0.4 on 2024-04-09 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token_access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('token', models.CharField(max_length=1000)),
            ],
        ),
    ]
