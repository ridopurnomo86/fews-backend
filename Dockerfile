FROM python:3.11

LABEL maintainer="fews.developer.proton.me"

ENV PYTHONUNBUFFERED 1

COPY . /app

COPY requirements.txt /app/requirements.txt

COPY .env /app/

WORKDIR /app

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000