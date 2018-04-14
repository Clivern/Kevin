FROM python:3

WORKDIR /www

RUN pip install -r requirements.txt
RUN ls
RUN ls /www

CMD [ "python", "./manage.py runserver 0.0.0.0:8000"]