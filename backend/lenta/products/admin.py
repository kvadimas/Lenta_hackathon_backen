from django.contrib import admin

from products.models import Categories, SalesData, SalesForecast, Stores, Holiday


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        "pr_sku_id",
        "pr_group_id",
        "pr_cat_id",
        "pr_subcat_id",
        "pr_uom_id",
    )
    list_filter = ("pr_group_id",)


@admin.register(SalesData)
class SalesDataAdmin(admin.ModelAdmin):
    list_display = (
        "pr_sku_id",
        "st_id",
        "date",
        "pr_sales_type_id",
        "pr_sales_in_units",
        "pr_promo_sales_in_units",
        "pr_sales_in_rub",
        "pr_promo_sales_in_rub",
    )
    list_filter = ("date",)


@admin.register(Stores)
class StoresAdmin(admin.ModelAdmin):
    list_display = (
        "st_id",
        "st_city_id",
        "st_division_code",
        "st_type_format_id",
        "st_type_loc_id",
        "st_type_size_id",
        "st_is_active",
    )
    list_filter = ("st_city_id",)


@admin.register(SalesForecast)
class SalesForecastAdmin(admin.ModelAdmin):
    list_display = (
        "st_id",
        "pr_sku_id",
        "date",
        "target",
    )
    list_filter = ("st_id",)


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = (
        "date",
        "holiday",
    )
