# HDesk
Web приложение для документирования IT инфраструктуры
[Demo](https://hdeskdemo.herokuapp.com/)
Логин: demo
Пароль: passdemo
# Обзор
Веб приложение позволяет:
* удобно добавлять и редактировать статьи (WYSIWYG)
* группировать статьи в разделы
* ставить метки и ориентироваться по меткам
* добавлять комментарии к статьям 
# Требования
* Python 3.5+
* Django 2.1+
* django-summernote
# Установка
* скачайте репозиторию: `git clone https://github.com/Ravillatypov/hdesk.git`
* перейдите в папу: `cd hdesk`
* установите необходимые пакеты: `pip install -r requirements.txt`
* отредактируйте настройки: `cp app/settings{,.prod}.py`
* настройте связку `gunicorn + systemd` (есть пример конфигурации в [папке](https://github.com/Ravillatypov/hdesk/tree/master/example_config))
* настройте прокси сервер nginx (есть пример конфигурации в [папке](https://github.com/Ravillatypov/hdesk/tree/master/example_config))
* выполните миграции: `./manage.py migrate`
* соберите статические файлы: `./manage.py collectstatic`
* добавьте ссылки для: `/static` и `/media`
* добавьте суперпользователя: `./manage.py createsuperuser`
# Отзывы и предложения
## Если нашли ошибку:
* По ошибкам безопасности напишите мне на [почту](mailto://latypov@iqvision.pro)
* По другим ошибка можете создать задачу по [ссылке](https://github.com/Ravillatypov/hdesk/issues/new)

[почта](mailto://latypov@iqvision.pro) для отзывыв и предложений