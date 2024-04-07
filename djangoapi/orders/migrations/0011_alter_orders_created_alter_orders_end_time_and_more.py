# Generated by Django 5.0.1 on 2024-04-07 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_orders_payer_name_alter_tradeorders_goods_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='created',
            field=models.DateTimeField(blank=True, help_text='创建时间', null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='end_time',
            field=models.DateTimeField(blank=True, help_text='结束时间', null=True, verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='modified',
            field=models.DateTimeField(blank=True, help_text='修改时间', null=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='pay_time',
            field=models.DateTimeField(blank=True, help_text='支付时间', null=True, verbose_name='支付时间'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='to_deliver_time',
            field=models.DateTimeField(blank=True, help_text='送货时间', null=True, verbose_name='送货时间'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='trade_time',
            field=models.DateTimeField(blank=True, help_text='下单时间', null=True, verbose_name='下单时间'),
        ),
    ]
