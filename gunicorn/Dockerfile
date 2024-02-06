# internet_shop/gunicorn/Dockerfile
FROM python:3.10

WORKDIR /app

ENV PYTHONPATH /app

# Установка gcc (если нужно)
RUN apt-get update && apt-get install -y gcc

# Установка Gunicorn
RUN pip install --no-cache-dir gunicorn==20.1.0

# Копирование конфигурационного файла Gunicorn и кода приложения
COPY gunicorn/gunicorn.conf.py .
COPY internet_shop/videostore /app

# Копирование файла зависимостей и установка их
COPY internet_shop/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000
EXPOSE 8000

# Переменная окружения, определяющая режим работы
#ENV RUN_ENV production

# Команда для запуска приложения (Gunicorn или runserver)
CMD ["sh", "-c", "export PYTHONPATH=/app && export DJANGO_SETTINGS_MODULE=videostore.videostore.settings && gunicorn --bind 0.0.0.0:8000 videostore.videostore.wsgi:application", "--chdir", "videostore"]

