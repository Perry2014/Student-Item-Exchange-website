# Generated by Django 5.0.1 on 2024-03-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_product_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sellermobileNum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='sellername',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
