# Generated by Django 5.0.1 on 2024-03-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_tradeorders_remove_orders_adjust_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='tid',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='原始单号'),
        ),
        migrations.AlterField(
            model_name='tradeorders',
            name='oid',
            field=models.CharField(blank=True, max_length=40, null=True, unique=True, verbose_name='原始子订单号'),
        ),
    ]