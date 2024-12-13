FROM python:3.12-slim as base

# Установка зависимостей для сборки
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Установка зависимостей
COPY ../src/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY ../src /app

# Экспорт переменной окружения для работы с Django в режиме разработки
ENV DJANGO_SETTINGS_MODULE=app.settings.dev

EXPOSE 8000

# Запускаем миграции и стартуем сервер
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]