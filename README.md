# yandex-backend

# This project is an entrance exam to the Yandex Backend School

# How to run the service?
1. Download the files from this repository
2. Make sure you have python >= 3.6.5 installed on your computer
3. Install the required modules from requirements.txt: $ pip (or pip3) install -r requirements.txt
4. Install gunicorn (or gunicorn3 if python3 is not your default Python): $ sudo apt-get install gunicorn (or gunicorn3)
5. Now everything is ready to run. Go to the project directory and start the service: $ gunicorn (or gunicorn3) -w 4 -b 0.0.0.0:8080 wsgi:app

# How to run the tests?
1. $ python (or python3) tester.py
