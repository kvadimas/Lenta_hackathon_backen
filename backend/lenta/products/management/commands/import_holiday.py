import csv

from django.core.management.base import BaseCommand
from progress.bar import IncrementalBar

from products.models import Holiday


class Command(BaseCommand):
    help = "Импонтировать данные из csv"

    def add_arguments(self, parser):
        """Использование опционального не обязательного аргумента"""
        parser.add_argument(
            "-d",
            "--delite",
            action="store_true",
            dest="delete_existing",
            default=False,
            help="Удалить существующие записи в таблице перед созданием новых",
        )

    def handle(self, *args, **options):
        """Метод импортирующий csv в базу данных"""
        if options["delete_existing"]:
            Holiday.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(
                    "Таблица Holiday очищена от старых записей."
                )
            )

        link = "test_data/holidays_calendar.csv"
        bar = IncrementalBar("Processing", max=3653)
        with open(link, encoding="utf-8") as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for i in dict_reader:
                Holiday.objects.get_or_create(**i)
                bar.next()
        self.stdout.write(self.style.SUCCESS(" Записи добавлены в таблицу."))
        bar.finish()
