# Generated by Django 3.2 on 2022-01-21 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0009_reviews'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={'verbose_name_plural': 'Reviews'},
        ),
        migrations.AddField(
            model_name='product',
            name='wishlisted',
            field=models.ManyToManyField(blank=True, to='profiles.UserProfile'),
        ),
    ]
