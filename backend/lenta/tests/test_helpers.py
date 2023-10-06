from products.models import Stores, Categories, SalesData, SalesForecast


def create_store():
    return Stores.objects.create(
        st_id="1",
        st_city_id="2",
        st_division_code="test_code",
        st_type_format_id=1,
        st_type_loc_id=2,
        st_type_size_id=3,
        st_is_active=True,
    )


def create_category():
    return Categories.objects.create(pr_sku_id="1", pr_group_id="2", pr_cat_id="3", pr_subcat_id="4", pr_uom_id=1)


def create_sales_data(category, store):
    return SalesData.objects.create(
        pr_sku_id=category,
        st_id=store,
        date="2022-10-20",
        pr_sales_type_id=True,
        pr_sales_in_units=10.5,
        pr_promo_sales_in_units=5.0,
        pr_sales_in_rub=100.0,
        pr_promo_sales_in_rub=50.0,
    )


def create_sales_forecast(category, store):
    return SalesForecast.objects.create(st_id=store, pr_sku_id=category, date="2022-10-20", target=100)
