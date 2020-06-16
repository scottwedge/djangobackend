# Generated by Django 3.0.2 on 2020-02-24 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_customers_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Customers'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='supplier_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.Supplier'),
        ),
    ]
