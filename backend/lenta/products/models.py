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
        null=True
    )
    st_division_code = models.CharField(
        'id дивизиона',
        max_length=50,
        null=True
    )
    st_type_format_id = models.IntegerField(
        'id формата магазина',
        null=True
    )
    st_type_loc_id = models.IntegerField(
        'id тип локации/окружения магазина',
        null=True
    )
    st_type_size_id = models.IntegerField(
        'id типа размера магазина',
        null=True
    )
    st_is_active = models.BooleanField('Флаг активного магазина', null=True)

    def __str__(self):
        return self.st_id

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class Categories(models.Model):
    pr_sku_id = models.CharField(
        'id товара',
        max_length=50,
        unique=True,
        primary_key=True
    )
    pr_group_id = models.CharField(
        'Группа товара',
        max_length=50,
        null=True
    )
    pr_cat_id = models.CharField(
        'Категория товара',
        max_length=50,
        null=True
    )
    pr_subcat_id = models.CharField(
        'Подкатегория товара',
        max_length=50,
        null=True
    )
    pr_uom_id = models.IntegerField(
        'Маркер',
        null=True
    )

    def __str__(self):
        return self.pr_sku_id

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class SalesData(models.Model):
    pr_sku_id = models.ForeignKey(
        Categories,
        null=True,
        on_delete=models.SET_NULL
    )
    st_id = models.ForeignKey(
        Stores,
        null=True,
        on_delete=models.SET_NULL
    )
    date = models.DateField('Дата', null=True)
    pr_sales_type_id = models.BooleanField('Промо', null=True)
    pr_sales_in_units = models.FloatField('Продажи без промо в шт.', null=True)
    pr_promo_sales_in_units = models.FloatField(
        'Продажи с промо в шт.',
        null=True
    )
    pr_sales_in_rub = models.FloatField('Продажи без промо в РУБ', null=True)
    pr_promo_sales_in_rub = models.FloatField(
        'Продажи с промо в РУБ',
        null=True
    )

    class Meta:
        verbose_name = 'Продажа'
        verbose_name_plural = 'Продажи'


class SalesForecast(models.Model):
    st_id = models.ForeignKey(
        Stores,
        null=True,
        on_delete=models.SET_NULL
    )
    pr_sku_id = models.ForeignKey(
        Categories,
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
