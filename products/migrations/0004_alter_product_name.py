# Generated by Django 3.2 on 2022-01-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220116_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, default='Unkown', max_length=254, null=True),
        ),
    ]
