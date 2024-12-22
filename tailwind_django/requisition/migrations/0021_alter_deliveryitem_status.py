# Generated by Django 5.1.3 on 2024-12-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requisition', '0020_alter_delivery_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryitem',
            name='status',
            field=models.CharField(choices=[('pending_delivery', 'Pending Delivery'), ('in_delivery', 'In Delivery'), ('received', 'Received'), ('delivered', 'Delivered')], default='pending_delivery', max_length=20),
        ),
    ]
