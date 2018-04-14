FROM python:3

RUN ls /opt

WORKDIR /opt

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000"]