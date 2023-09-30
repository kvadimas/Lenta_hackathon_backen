from datetime import datetime

from rest_framework.serializers import ModelSerializer, ValidationError

from products.models import (
    Stores as Shopes,
    Categories,
    SalesData as Sales,
    SalesForecast as Forecast,
)


class CastomSerializer(ModelSerializer):
    """Обединяет некоторые патерны валидации."""

    def validate_string_length(self, field_name, value):
        if len(value) > 50:
            raise ValidationError(
                f"Некорректный размер поля {field_name}. " "Размер должен быть не больше 50 символов."
            )
        return value

    def validate_type(self, field_name, value, required_type):
        if not isinstance(value, required_type):
            raise ValidationError(f"Значение поля {field_name} должно быть типа " f"{required_type.__name__}.")
        return value

    def validate_date(self, value):
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            raise ValidationError("Значение поля date должно быть в формате YYYY-MM-DD.")
        return value


class ShopesSerializer(CastomSerializer):
    class Meta:
        model = Shopes
        fields = "__all__"

    def validate_st_id(self, value):
        if not value:
            raise ValidationError("id магазина- обязательное поле.")
        if len(value) > 50:
            raise ValidationError("Некорректный id магазина.", "Размер должен быть не больше 50 символов.")
        if self.Meta.model.objects.filter(st_id=value).exists():
            raise ValidationError("Уже существует магазин с таким id.")
        return value

    def validate_st_city_id(self, value):
        return self.validate_string_length("id города", value)

    def validate_st_division_code(self, value):
        return self.validate_string_length("id дивизиона", value)

    def validate_st_type_format_id(self, value):
        return self.validate_type("id формата магазина", value, int)

    def validate_st_type_size_id(self, value):
        return self.validate_type("id типа размера магазина", value, int)

    def validate_st_is_active(self, value):
        return self.validate_type("флаг активного магазина", value, bool)


class CategoriesSerializer(CastomSerializer):
    class Meta:
        model = Categories
        fields = "__all__"

    def validate_pr_sku_id(self, value):
        if not value:
            raise ValidationError("id товара- обязательное поле.")
        if len(value) > 51:
            raise ValidationError("Некорректный id товара.", "Размер должен быть не больше 50 символов.")
        if self.Meta.model.objects.filter(st_id=value).exists():
            raise ValidationError("Уже существует товар с таким id.")
        return value

    def validate_pr_group_id(self, value):
        return self.validate_string_length("группа товара", value)

    def validate_pr_cat_id(self, value):
        return self.validate_string_length("категория товара", value)

    def validate_pr_subcat_id(self, value):
        return self.validate_string_length("подкатегория товара", value)

    def validate_pr_uom_id(self, value):
        return self.validate_type("маркер", value, int)


class SalesSerializer(CastomSerializer):
    class Meta:
        model = Sales
        fields = "__all__"

    def validate_pr_sku_id(self, value):
        n = None
        if not (self.Meta.model.objects.filter(pr_sku_id=value).exists() or n):
            raise ValidationError(f"{value} не id товара.")
        return value

    def validate_st_id(self, value):
        if not (self.Meta.model.objects.filter(st_id=value).exists() or None):
            raise ValidationError(f"{value} не id магазина.")
        return value

    def validate_pr_sales_type_id(self, value):
        return self.validate_type("промо", value, bool)

    def validate_pr_sales_in_units(self, value):
        return self.validate_type("pr_sales_in_units", value, float)

    def validate_pr_promo_sales_in_units(self, value):
        return self.validate_type("pr_promo_sales_in_units", value, float)

    def validate_pr_sales_in_rub(self, value):
        return self.validate_type("pr_sales_in_rub", value, float)

    def validate_pr_promo_sales_in_rub(self, value):
        return self.validate_type("pr_promo_sales_in_rub", value, float)


class ForecastSerializer(CastomSerializer):
    class Meta:
        model = Forecast
        fields = "__all__"

    def validate_st_id(self, value):
        if not (self.Meta.model.objects.filter(st_id=value).exists() or None):
            raise ValidationError(f"{value} не id магазина.")
        return value

    def validate_pr_sku_id(self, value):
        if not (self.Meta.model.objects.filter(pr_sku_id=value).exists()):
            raise ValidationError(f"{value} не id товара.")
        return value

    def validate_target(self, value):
        if not isinstance(value, int):
            raise ValidationError("Значение поля спрос должно быть типа int.")
        if value < 0:
            raise ValidationError("Значение поля спрос должно быть больше ноля.")
        return value
