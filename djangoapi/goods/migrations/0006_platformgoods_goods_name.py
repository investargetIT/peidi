# Generated by Django 5.0.1 on 2024-04-19 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_remove_platformgoods_disable_syn_until_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformgoods',
            name='goods_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='货品名称'),
        ),
    ]
