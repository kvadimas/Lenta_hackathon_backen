FROM python:3.11

WORKDIR /app

COPY lenta/requirements.txt .

RUN pip3 install --upgrade pip && pip3 install -r /app/requirements.txt --no-cache-dir

COPY lenta/ .