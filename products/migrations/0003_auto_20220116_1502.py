# Generated by Django 3.2 on 2022-01-16 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220116_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='year',
        ),
        migrations.AlterField(
            model_name='product',
            name='artist_name',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=254),
        ),
    ]
