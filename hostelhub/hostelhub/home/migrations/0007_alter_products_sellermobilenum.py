# Generated by Django 5.0.1 on 2024-03-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_products_sellermobilenum_products_sellername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='sellermobileNum',
            field=models.CharField(),
        ),
    ]
