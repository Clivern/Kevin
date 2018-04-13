FROM django

ADD . /kevin

WORKDIR /kevin

RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
