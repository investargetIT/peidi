# Generated by Django 5.0.1 on 2024-05-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_exchangemanagement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangemanagement',
            name='trade_no',
            field=models.CharField(blank=True, max_length=512, null=True, verbose_name='系统订单'),
        ),
    ]
