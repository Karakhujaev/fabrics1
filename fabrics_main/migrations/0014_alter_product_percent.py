# Generated by Django 4.1.5 on 2023-05-10 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrics_main', '0013_alter_product_selling_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='percent',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]