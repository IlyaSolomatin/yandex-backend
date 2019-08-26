# yandex-backend

# Как запустить сервис?
1. Скачайте файлы из данного репозитория
2. Убедитесь, что на вашем компьютере есть python>=3.6.5
3. Установите необходимые модули из requirements.txt: $ pip (или pip3) install -r requirements.txt
4. Установите gunicorn (или gunicorn3, если python3 не является основным питоном): $ sudo apt-get install gunicorn (или gunicorn3)
5. Теперь все готово к запуску. Перейдите в директорию проекта и запустите $ gunicorn (или gunicorn3) -w 4 -b 0.0.0.0:8080 wsgi:app

# Как запустить тесты?
1. $ python (или python3) tester.py
