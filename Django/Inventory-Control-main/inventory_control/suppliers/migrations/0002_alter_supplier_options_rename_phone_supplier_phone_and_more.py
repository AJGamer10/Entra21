# Generated by Django 5.0.1 on 2024-01-23 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='PHONE',
            new_name='phone',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
