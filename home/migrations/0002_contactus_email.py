# Generated by Django 3.2 on 2022-01-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='email',
            field=models.EmailField(default='non', max_length=254),
        ),
    ]
