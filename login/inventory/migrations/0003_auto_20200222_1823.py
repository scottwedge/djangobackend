# Generated by Django 3.0.2 on 2020-02-22 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200222_1820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='parent_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Product'),
        ),
    ]