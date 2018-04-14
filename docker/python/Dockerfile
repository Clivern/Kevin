FROM python:3

RUN ls /opt/
RUN ls /opt/www/

WORKDIR /opt/www/

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000"]