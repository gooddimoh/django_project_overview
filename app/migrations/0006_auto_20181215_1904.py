# Generated by Django 2.0.6 on 2018-12-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_standard_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='default name', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='keyword',
            field=models.CharField(default='default name', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(default='default name', max_length=300),
        ),
    ]
