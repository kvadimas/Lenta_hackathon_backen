from openpyxl import Workbook
from io import BytesIO


def get_report():
    products = [
        ("батон", "пятерочка", 1500, 9.95),
        ("молоко", "лента", 600, 4.95),
        ("сыр", "дикси", 200, 19.95),
        ("вода", "7/11", 2000, 49.95),
    ]
    wb = Workbook()
    list = wb.active
    # Создание строки с заголовками
    list.append(("Название", "Магазин", "Количество", "Цена"))
    for product in products:
        list.append(product)
    buffer = BytesIO()
    wb.save(buffer)
    return buffer


a = get_report()
with open("my_report.xlsx", "wb") as f:
    f.write(a.getvalue())
