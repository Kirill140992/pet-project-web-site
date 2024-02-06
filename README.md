# pet-project-web-site

Мой пет- проект. Кратко, что в нем есть:

Все делается в контейнерах(Docker);
Балансировщик - NGINX;
Сайт написанный на Django, на нем есть возможность добавлять контент, авторизация и личный кабинет(в планах отправка писем при регистрации). Неожиданно для меня познакомился с Gunicorn, притормозил он меня ;
Redis - для кэширования;
PostgreSQL, репликация Master-Slave;
ProxySQL для проксирования PostgreSQL;
RabbitMQ, как брокер очереди для отправки писем о регистрации в SendGrid;
Логгирование ELK;
Prometheus + Grafana для визуализации и Slack для отправки алертов;
CI/CD на Jenkins+Gitlab(пока вопрос как это сделать, изучаю)
Для эксплуатации и развертывания Terraform и Ansible;
Оркестратор Kubernetes с применением Helm;
Сервера для развертывания AWS(так как лидер рынка) и YandexCloud(личная симпатия).
Опционально, что хочу добавить после основной части:

MongoDB;
Clickhouse;
Telegram-bot;
Zookeeper.
Что сделано сейчас:

NGINX;
Gunicorn + Django;
ProxySQL;
PostgreSQL.