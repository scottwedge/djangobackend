# Generated by Django 3.0.2 on 2020-02-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_product_supplier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
