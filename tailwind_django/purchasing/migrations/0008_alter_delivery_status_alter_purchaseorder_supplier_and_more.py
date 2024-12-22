# Generated by Django 5.1.4 on 2024-12-12 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0007_globalsettings_inventoryitem_description_and_more"),
        ("purchasing", "0007_delivery_delivery_confirmation_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending_delivery", "Pending Delivery"),
                    ("in_transit", "In Transit"),
                    ("in_delivery", "In Delivery"),
                    ("delivered", "Delivered"),
                    ("verified", "Verified"),
                    ("completed", "Completed"),
                    ("cancelled", "Cancelled"),
                ],
                default="pending_delivery",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="supplier",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchase_orders",
                to="purchasing.supplier",
            ),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="warehouse",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="purchase_orders",
                to="inventory.warehouse",
            ),
        ),
    ]
