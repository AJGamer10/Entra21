# Generated by Django 5.0.1 on 2024-01-30 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_product_suppliers_productsinventory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductsInventory',
            new_name='ProductInventory',
        ),
    ]
