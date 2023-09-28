from django.db import models


class Stores(models.Model):
    st_id = models.CharField(
        'id магазина',
        max_length=50,
        unique=True,
        primary_key=True
    )
    st_city_id = models.CharField(
        'id города',
        max_length=50,
        unique=True
    )
    st_division_code = models.CharField(
        'id дивизиона',
        max_length=50,
        unique=True
    )
    st_type_format_id = models.IntegerField(
        'id формата магазина',
        unique=True
    )
    st_type_loc_id = models.IntegerField(
        'id тип локации/окружения магазина',
        unique=True
    )
    st_type_size_id = models.IntegerField(
        'id типа размера магазина',
        unique=True
    )
    st_is_active = models.BooleanField('Флаг активного магазина')

    def __str__(self):
        return self.st_id

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Product(models.Model):
    pr_sku_id = models.CharField(
        'id товара',
        max_length=50,
        unique=True,
        primary_key=True
    )
    pr_group_id = models.CharField(
        'Группа товара',
        max_length=50,
        unique=True
    )
    pr_cat_id = models.CharField(
        'Категория товара',
        max_length=50,
        unique=True
    )
    pr_subcat_id = models.CharField(
        'Подкатегория товара',
        max_length=50,
        unique=True
    )
    pr_uom_id = models.IntegerField(
        'Маркер',
        unique=True
    )
    st_id = models.ForeignKey(
        Stores,
        null=True,
        on_delete=models.SET_NULL
    )
    date = models.DateField('Дата')
    pr_sales_type_id = models.BooleanField('Промо')
    pr_sales_in_units = models.FloatField('Продажи без промо в шт.')
    pr_promo_sales_in_units = models.FloatField('Продажи с промо в шт.')
    pr_sales_in_rub = models.FloatField('Продажи без промо в РУБ')
    pr_promo_sales_in_rub = models.FloatField('Продажи с промо в РУБ')

    def __str__(self):
        return self.pr_sku_id

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Продукты'


class SalesForecast(models.Model):
    st_id = models.ForeignKey(
        Stores,
        null=True,
        on_delete=models.SET_NULL
    )
    pr_sku_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    date = models.DateField('Дата')
    target = models.IntegerField(
        'Спрос в шт',
        default=0
    )

    class Meta:
        verbose_name = 'Спрос'
        verbose_name_plural = 'Спрос'
