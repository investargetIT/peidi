# Generated by Django 5.0.1 on 2024-05-10 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_tmallrefund_goods_return_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DouyinRefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺名称')),
                ('pay_transaction_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='支付流水号')),
                ('trade_no', models.CharField(max_length=100, verbose_name='订单编号')),
                ('goods_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品名称')),
                ('goods_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='商品ID')),
                ('refund_reason', models.CharField(blank=True, max_length=255, null=True, verbose_name='打款类型')),
                ('refund', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='打款金额')),
                ('applicant', models.CharField(blank=True, max_length=100, null=True, verbose_name='打款申请人')),
                ('apply_time', models.DateTimeField(blank=True, null=True, verbose_name='打款申请时间')),
                ('refund_time', models.DateTimeField(blank=True, null=True, verbose_name='打款到账时间')),
                ('refund_status', models.CharField(blank=True, max_length=40, null=True, verbose_name='打款状态')),
                ('refund_remark', models.CharField(blank=True, max_length=1024, null=True, verbose_name='打款备注')),
            ],
        ),
        migrations.CreateModel(
            name='JdRefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺名称')),
                ('apply_time', models.DateTimeField(blank=True, null=True, verbose_name='申请时间')),
                ('refund_no', models.CharField(max_length=100, verbose_name='赔付单号')),
                ('trade_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='关联订单号')),
                ('service_no', models.CharField(blank=True, max_length=100, null=True, verbose_name='关联服务单号')),
                ('refund', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='赔付金额')),
                ('refund_reason', models.CharField(blank=True, max_length=255, null=True, verbose_name='赔付原因')),
                ('refund_status', models.CharField(blank=True, max_length=40, null=True, verbose_name='赔付状态')),
                ('applicant', models.CharField(blank=True, max_length=100, null=True, verbose_name='申请人')),
            ],
        ),
        migrations.CreateModel(
            name='PddRefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='店铺名称')),
                ('trade_no', models.CharField(max_length=100, verbose_name='订单号')),
                ('goods_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='商品ID')),
                ('goods_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='商品名称')),
                ('refund_reason', models.CharField(blank=True, max_length=255, null=True, verbose_name='扣款原因')),
                ('applicant', models.CharField(blank=True, max_length=100, null=True, verbose_name='申请人')),
                ('apply_time', models.DateTimeField(blank=True, null=True, verbose_name='申请时间')),
                ('refund', models.DecimalField(blank=True, decimal_places=4, max_digits=19, null=True, verbose_name='申请扣款金额')),
                ('refund_status', models.CharField(blank=True, max_length=40, null=True, verbose_name='打款状态')),
            ],
        ),
        migrations.AlterField(
            model_name='tmallrefund',
            name='refund_explanation',
            field=models.CharField(blank=True, max_length=1024, null=True, verbose_name='买家退款说明'),
        ),
        migrations.AddConstraint(
            model_name='douyinrefund',
            constraint=models.UniqueConstraint(fields=('pay_transaction_no', 'trade_no', 'goods_id'), name='unique_paytransactionno_tradeno_goodsid'),
        ),
        migrations.AddConstraint(
            model_name='jdrefund',
            constraint=models.UniqueConstraint(fields=('refund_no', 'trade_no', 'service_no'), name='unique_refundno_tradeno_serviceno'),
        ),
        migrations.AddConstraint(
            model_name='pddrefund',
            constraint=models.UniqueConstraint(fields=('trade_no', 'goods_id'), name='unique_tradeno_goodsid'),
        ),
    ]
