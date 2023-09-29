import csv

from django.apps import apps
from django.core.management.base import BaseCommand
from progress.bar import IncrementalBar


class Command(BaseCommand):
    help = 'Импонтировать данные из csv'

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
        bar = IncrementalBar('Processing', max=20)
        models = ['Stores', 'Product']#, 'SalesForecast' 'Product'
        links = [
            'test_data/st_df.csv',
            ['test_data/st_df.csv','test_data/sales_df_train.csv'],
            'test_data/sales_submission.csv'
        ]
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
                bar.next

            # Подсчет добавляемых строк
            count_row = 0

            # Запись
            if _name == 'Product':
                with open(link[0], encoding='utf-8') as csvfile0:
                    dict_reader0 = csv.DictReader(csvfile0)
                    with open(link[1], encoding='utf-8') as csvfile1:
                        dict_reader1 = csv.DictReader(csvfile1)
                        dict0 = [i for i in dict_reader0]
                        dict1 = [j for j in dict_reader1]
                        print(dict0)
                continue


            with open(link, encoding='utf-8') as csvfile:
                dict_reader = csv.DictReader(csvfile)
                for i in dict_reader:
                    count_row += 1
                    _model.objects.get_or_create(**i)
                    bar.next
                self.stdout.write(
                    self.style.SUCCESS(
                        f'Добавлено {count_row} записей в таблицу {_name}.'
                    )
                )
            bar.finish()
