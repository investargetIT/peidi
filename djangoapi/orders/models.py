from django.db import models

# Create your models here.



class orders(models.Model):
    platform = models.CharField(max_length=20, blank=True, null=True, verbose_name='平台')
    shop_name = models.CharField(max_length=20, blank=True, null=True, verbose_name='店铺')
    tid = models.CharField(max_length=40, blank=True, null=True, unique=True, verbose_name='原始单号')
    warehouse_no = models.CharField(max_length=20, blank=True, null=True, verbose_name='外部仓库编号')
    trade_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台状态')
    pay_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='支付状态')
    guarantee_mode = models.CharField(max_length=40, blank=True, null=True, verbose_name='担保方式')
    delivery_term = models.CharField(max_length=40, blank=True, null=True, verbose_name='货到付款')
    pay_method = models.CharField(max_length=40, blank=True, null=True, verbose_name='支付方式')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款状态')
    process_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='系统处理状态')
    bad_reason = models.TextField(blank=True, null=True, verbose_name='递交失败原因')
    trade_time = models.DateTimeField(blank=True, null=True, help_text='下单时间')
    pay_time = models.DateTimeField(blank=True, null=True, help_text='支付时间')
    end_time = models.DateTimeField(blank=True, null=True, help_text='结束时间')
    buyer_nick = models.CharField(max_length=100, blank=True, null=True, verbose_name='客户网名')
    receiver_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='收件人姓名')
    receiver_area = models.CharField(max_length=128, blank=True, null=True, verbose_name='省市县')
    receiver_ring = models.CharField(max_length=20, blank=True, null=True, verbose_name='区域（京东几环）')
    receiver_address = models.CharField(max_length=255, blank=True, null=True, verbose_name='收件人地址')
    receiver_mobile = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人手机')
    receiver_telno = models.CharField(max_length=40, blank=True, null=True, verbose_name='收件人电话')
    receiver_zip = models.CharField(max_length=20, blank=True, null=True, verbose_name='收件人邮编')
    to_deliver_time = models.DateTimeField(blank=True, null=True, help_text='送货时间')
    buyer_message = models.CharField(max_length=1024, blank=True, null=True, verbose_name='买家备注')
    remark = models.CharField(max_length=1024, blank=True, null=True, verbose_name='客服备注')
    biaoqi = models.CharField(max_length=100, blank=True, null=True, verbose_name='标旗')
    goods_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货款')
    post_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='邮费')
    other_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='其他收费')
    discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='优惠')
    platform_cost = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台费用')
    received = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已收')
    receivable = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='应收')
    cash_on_delivery_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='货到付款金额')
    refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退款金额')
    logistics_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='物流方式')
    invoice_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='发票类别',
                                     help_text='普通发票/电子发票/专用发票/全电普通发票/全电专用发票')
    payer_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='对应发票抬头，付款方名称')
    invoice_content = models.TextField(blank=True, null=True, verbose_name='发票内容')
    is_auto_wms = models.CharField(max_length=40, blank=True, null=True, verbose_name='是否自流转')
    is_ware_trade = models.CharField(max_length=40, blank=True, null=True, verbose_name='外部订单')
    trade_from = models.CharField(max_length=40, blank=True, null=True, verbose_name='订单来源')
    logistics_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='物流编码')
    pay_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='支付单号')
    pay_account = models.CharField(max_length=128, blank=True, null=True, verbose_name='买家支付账号')
    paid = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='已付')
    consumer_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='消费者实付金额')
    platform_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='平台承担优惠金额')
    currency = models.TextField(blank=True, null=True, verbose_name='币种')
    id_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='证件号码')
    modified = models.DateTimeField(blank=True, null=True, help_text='修改时间')
    created = models.DateTimeField(blank=True, null=True, help_text='创建时间')

class tradeOrders(models.Model):
    tid = models.CharField(max_length=40, blank=True, null=True, verbose_name='原始单号')
    oid = models.CharField(max_length=40, blank=True, null=True, unique=True, verbose_name='原始子订单号')
    status = models.CharField(max_length=40, blank=True, null=True, verbose_name='状态')
    process_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='处理状态')
    refund_status = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款状态')
    order_type = models.CharField(max_length=40, blank=True, null=True, verbose_name='子订单类型')
    goods_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台货品id')
    spec_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='平台规格id')
    goods_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='货品编号')
    spec_no = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格编码')
    goods_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='货品名称')
    spec_name = models.CharField(max_length=40, blank=True, null=True, verbose_name='规格名称')
    num = models.IntegerField(blank=True, null=True, verbose_name='数量')
    price = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='单价')
    adjust_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='调整')
    discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='优惠')
    total_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='总价')
    share_discount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊优惠')
    share_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='分摊后应收')
    refund_amount = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True, verbose_name='退款金额')
    refund_id = models.CharField(max_length=40, blank=True, null=True, verbose_name='退款单编号')
    end_time = models.DateTimeField(blank=True, null=True, help_text='子单完成时间')
    modified = models.DateTimeField(blank=True, null=True, help_text='修改时间')
    created = models.DateTimeField(blank=True, null=True, help_text='创建时间')
    image = models.CharField(max_length=128, blank=True, null=True, verbose_name='图片')
    sys_goods_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='系统货品名称')
    sys_spec_name = models.CharField(max_length=128, blank=True, null=True, verbose_name='系统规格名称')