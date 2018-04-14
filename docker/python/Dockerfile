FROM python:3

RUN ls /var
RUN ls /var/www

WORKDIR /var/www

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000"]