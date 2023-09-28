from django.contrib import admin

from products.models import Product, SalesForecast, Stores


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pr_sku_id',
        'pr_group_id',
        'pr_cat_id',
        'pr_subcat_id',
        'pr_uom_id',
        'st_id',
        'date',
        'pr_sales_type_id',
        'pr_sales_in_units',
        'pr_promo_sales_in_units',
        'pr_sales_in_rub',
        'pr_promo_sales_in_rub'
    )
    list_filter = ('pr_group_id', 'pr_cat_id', 'pr_subcat_id', 'date')


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display = (
        'st_id',
        'st_city_id',
        'st_division_code',
        'st_type_format_id',
        'st_type_loc_id',
        'st_type_size_id',
        'st_is_active',
    )
    list_filter = (
        'st_city_id',
        'st_division_code',
    )


@admin.register(SalesForecast)
class SalesForecastAdmin(admin.ModelAdmin):
    list_display = (
        'st_id',
        'pr_sku_id',
        'date',
        'target',
    )
    list_filter = (
        'st_id',
        'pr_sku_id',
    )
