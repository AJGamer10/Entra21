# Generated by Django 5.0.1 on 2024-01-30 23:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_category_slug_supplierproduct_and_more'),
        ('suppliers', '0002_alter_supplier_options_rename_phone_supplier_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='suppliers',
            field=models.ManyToManyField(blank=True, through='products.SupplierProduct', to='suppliers.supplier'),
        ),
        migrations.CreateModel(
            name='ProductsInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=8)),
                ('local', models.CharField(max_length=255)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'verbose_name': 'Inventário de produtos',
                'verbose_name_plural': 'Inventário de produtos',
            },
        ),
    ]
