FROM python:3.10
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
COPY ./videostore/manage.py .
EXPOSE 8000
CMD ["sh", "-c", "export PYTHONPATH=/app && export DJANGO_SETTINGS_MODULE=videostore.videostore.settings && gunicorn --bind 0.0.0.0:8000 videostore.videostore.wsgi:application", "--chdir", "videostore"]
