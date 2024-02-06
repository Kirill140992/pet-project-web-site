# gunicorn.conf.py
import multiprocessing

bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
module = 'videostore.wsgi:application'
env = 'DJANGO_SETTINGS_MODULE=videostore.videostore.settings'
