# Generated by Django 5.0.1 on 2024-03-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suitegoodsrec',
            name='barcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='条码'),
        ),
        migrations.AlterField(
            model_name='suitegoodsrec',
            name='is_fixed_price',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='是否固定价格'),
        ),
        migrations.AlterField(
            model_name='suitegoodsrec',
            name='spec_code',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='规格码'),
        ),
        migrations.AlterField(
            model_name='suitegoodsrec',
            name='spec_no',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='商家编码'),
        ),
        migrations.AlterField(
            model_name='suitegoodsrec',
            name='suite_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='组合装名称'),
        ),
    ]
