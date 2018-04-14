FROM python:3

RUN mkdir /kevin
WORKDIR /kevin
ADD . /kevin

RUN ls
RUN rm .env
RUN cp .env.docker .env
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py migrate

CMD [ "python", "./manage.py runserver 0.0.0.0:8000"]