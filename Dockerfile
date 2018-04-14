FROM python:3

RUN mkdir /kevin
WORKDIR /kevin
ADD . /kevin

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD [ "python", "./manage.py runserver 0.0.0.0:8000"]