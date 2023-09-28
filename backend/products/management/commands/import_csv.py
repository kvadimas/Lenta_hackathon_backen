import csv
import timeit

from django.apps import apps
from django.core.management.base import BaseCommand
from progress.bar import IncrementalBar

from products.models import Categories, Stores


class Command(BaseCommand):
    help = 'Импонтировать данные из csv'

    def write_to_database(self, link, _model, count_row, _name):
        bar = IncrementalBar('Processing', max=20)
        with open(link, encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)

            if _name == 'SalesData':
                records = []
                for i in dict_reader:
                    record = _model(
                        st_id=Stores.objects.get_or_create(
                            st_id=i['st_id']
                        )[0],
                        pr_sku_id=Categories.objects.get_or_create(
                            pr_sku_id=i['pr_sku_id']
                        )[0],
                        date=i['date'],
                        pr_sales_type_id=i['pr_sales_type_id'],
                        pr_sales_in_units=i['pr_sales_in_units'],
                        pr_promo_sales_in_units=i['pr_promo_sales_in_units'],
                        pr_sales_in_rub=i['pr_sales_in_rub'],
                        pr_promo_sales_in_rub=i['pr_promo_sales_in_rub']
                    )
                    records.append(record)
                    count_row += 1
                    bar.next()
                _model.objects.bulk_create(records)
                bar.finish()
                return count_row

            if _name == 'SalesForecast':
                records = []
                for i in dict_reader:
                    record = _model(
                        st_id=Stores.objects.get_or_create(
                            st_id=i['st_id']
                        )[0],
                        pr_sku_id=Categories.objects.get_or_create(
                            pr_sku_id=i['pr_sku_id']
                        )[0],
                        date=i['date'],
                        target=i['target']
                    )
                    records.append(record)
                    count_row += 1
                    bar.next()
                _model.objects.bulk_create(records)
                bar.finish()
                return count_row

            # Остальные случаи
            for i in dict_reader:
                count_row += 1
                _model.objects.get_or_create(**i)
                bar.next()
        bar.finish()
        return count_row

    def add_arguments(self, parser):
        '''Использование опционального не обязательного аргумента'''
        parser.add_argument(
            '-d',
            '--delite',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Удалить существующие записи в таблице перед созданием новых',
        )

    def handle(self, *args, **options):
        '''Метод импортирующий csv в базу данных'''
        models = [
            'Stores',
            'Categories',
            'SalesData',
            'SalesForecast']
        links = [
            'test_data/st_df.csv',
            'test_data/pr_df.csv',
            'test_data/sales_df_train.csv',
            'test_data/sales_submission.csv'
        ]
        start_time = timeit.default_timer()
        for _name, link in zip(models, links):
            try:
                _model = apps.get_model('products', _name)
            except Exception:
                self.stdout.write(
                    self.style.ERROR(
                        'Ошибка при импорте модели!'
                    )
                )

            if options['delete_existing']:
                _model.objects.all().delete()
                self.stdout.write(
                    self.style.WARNING(
                        f'Таблица {_name} очищена от старых записей.'
                    )
                )

            # Подсчет добавляемых строк
            count_row = 0

            # Запись
            #try:
            self.write_to_database(link, _model, count_row, _name)
            elapsed_time = timeit.default_timer() - start_time
            print(f'Время выполнения: {elapsed_time:.2f} секунд')
            self.stdout.write(
                self.style.SUCCESS(
                    f'Добавлено {count_row} записей в таблицу {_name}.'
                )
            )
            #except:
            #    self.stdout.write(
            #        self.style.ERROR(
            #            f'Ошибка при добавлении записей в таблицу {_name}.'
            #        )
            #    )
