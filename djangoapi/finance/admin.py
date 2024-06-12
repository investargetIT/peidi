from django.contrib import admin
from .models import TmallRefund, PddRefund, JdRefund, DouyinRefund, Invoice, GoodsSalesSummary, FinanceSalesAndInvoice, PDMaterialNOList
from rangefilter.filters import DateRangeFilterBuilder

@admin.register(TmallRefund)
class TmallRefundAdmin(admin.ModelAdmin): 
    list_display = [
        "refund_no",
        "trade_no",
        "alipay_transaction_no",
        "pay_time",
        "goods_no",
        "refund_close_time",
        "paid",
        "goods_name",
        "refund",
        "refund_source",
        "goods_return",
        "apply_time",
        "refund_deadline",
        "refund_status",
        "goods_status",
        "deliver_logistics_info",
        "service_intervene",
        "seller_name",
        "seller_name_new",
        "refund_reason",
        "refund_explanation",
        "refund_type",
    ]
    list_filter = (
        (
            "apply_time",
            DateRangeFilterBuilder(
                title="退款的申请时间",
            ),
        ),
    )
    search_fields = ["trade_no", "goods_no", "goods_name"]

@admin.register(PddRefund)
class PddRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "trade_no",
        "goods_id",
        "goods_name",
        "refund_reason",
        "applicant",
        "apply_time",
        "refund",
        "refund_status"
    ]
    list_filter = (
        (
            "apply_time",
            DateRangeFilterBuilder(
                title="申请时间",
            ),
        ),
    )

@admin.register(JdRefund)
class JdRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "apply_time",
        "refund_no",
        "trade_no",
        # "service_no",
        "refund",
        "refund_reason",
        "refund_status",
        "applicant",
    ]
    list_filter = (
        (
            "apply_time",
            DateRangeFilterBuilder(
                title="申请时间",
            ),
        ),
    )

@admin.register(DouyinRefund)
class DouyinRefundAdmin(admin.ModelAdmin):
    list_display = [
        "shop_name",
        "pay_transaction_no",
        "trade_no",
        "goods_name",
        "goods_id",
        "refund_reason",
        "refund",
        "applicant",
        "apply_time",
        "refund_time",
        "refund_status",
        "refund_remark",
    ]
    list_filter = (
        (
            "refund_time",
            DateRangeFilterBuilder(
                title="打款到账时间",
            ),
        ),
    )

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "trade_no",
        "invoice_time",
        "shop_name",
        # "invoice_category",
        # "invoice_type",
        # "invoice_no",
        # "seller_tax_no",
        # "seller_corp_name",
        # "invoice_title",
        # "payer_tax_no",
        # "invoice_tax",
        # "invoice_amount",
        # "red_to_blue",
        # "remark",
        "goods_name",
        "goods_model",
        "goods_unit",
        "goods_price",
        "goods_num",
        "goods_amount_without_tax",
        "goods_tax",
        "goods_total_amount",
        "tax_rate",
    ]
    search_fields = ["trade_no", "goods_model"]
    list_filter = ["shop_name"]

@admin.register(GoodsSalesSummary)
class GoodsSalesSummaryAdmin(admin.ModelAdmin):
    list_display = [
        "start_date",
        "end_date",
        "spec_no",
        "major_supplier",
        "shop_name",
        "brand_name",
        "goods_type",
        "goods_no",
        "goods_name",
        "spec_name",
        "goods_type",
        "average_price",
        "retail_price",
        "ship_num",
        "return_num",
        "return_count_num",
        "sales_num",
        "ship_amount",
        "sales_amount",
        "sales_amount_unknown_cost",
        "return_amount",
        "actual_sales_amount",
        "gift_sales_num",
        "post_amount",
        "post_cost",
        "ship_refund_num",
        "ship_refund_amount",
        "abnormal_warehouse_sales_num",
        "refund_stockin",
    ]

@admin.register(FinanceSalesAndInvoice)
class FinanceSalesAndInvoiceAdmin(admin.ModelAdmin):
    list_display = [
        "created_at",
        "start_date",
        "end_date",
        "date",
        "shop_name",
        "goods_no",
        "material_no",
        "goods_name",
        "sales_num",
        "invoice_num",
        "sales_amount",
        "post_amount",
        "refund_amount",
        "invoice_amount",
    ]
    search_fields = ["goods_no"]
    list_filter = (
        (
            "date",
            DateRangeFilterBuilder(
                title="开票/退款时间",
            ),
        ),
    )

@admin.register(PDMaterialNOList)
class PDMaterialNOListAdmin(admin.ModelAdmin):
    list_display = [
        "material_no",
        "type",
        "goods_name",
        "invoice_goods_name",
        "goods_no",
        "no_product_series",
        "barcode",
        "unit",
        "feature",
        "brand",
        "weight",
    ]
    search_fields = ["material_no", "goods_name", "goods_no", "barcode"]
