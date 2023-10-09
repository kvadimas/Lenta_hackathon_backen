from openpyxl import Workbook
from io import BytesIO


def get_report(data):

    wb = Workbook()
    ws = wb.active
    # Создание строки с заголовками
    title = list(data["import"][0].keys())
    ws.append(title)
    prod = [tuple(val.values()) for dicts in data["import"] for val in dicts]
    for line in prod:
        ws.append(line)
    buffer = BytesIO()
    wb.save(buffer)
    return buffer
