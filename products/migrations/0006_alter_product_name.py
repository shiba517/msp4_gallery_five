# Generated by Django 3.2 on 2022-01-16 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20220116_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='Unknown', max_length=254),
        ),
    ]