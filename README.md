# Kevin
Web Application to Inspect HTTP Requests & Build Custom Endpoints.

[![Build Status](https://travis-ci.org/Clivern/Kevin.svg?branch=master)](https://travis-ci.org/Clivern/Kevin)

Installation
------------

In order to run this app do the following:

### Default Install

- Get the application code

```bash
git clone https://github.com/Clivern/Kevin.git kevin
cd kevin
cp .env.example .env
```

- Install dependencies

```bash
pip install -r requirements.txt
```

- Edit the .env file manually or use command for that

```bash
# Set DB Host
python manage.py kevin update_env DB_HOST=127.0.0.1

# Set DB Port
python manage.py kevin update_env DB_PORT=3306

# Set DB Name
python manage.py kevin update_env DB_DATABASE=kevin

# Set DB Username
python manage.py kevin update_env DB_USERNAME=root

# Set DB Password
python manage.py kevin update_env DB_PASSWORD=

# Create a new app key (Required)
python manage.py kevin update_app_key

# Set DB Type (mysql or sqlite supported till now)
python manage.py kevin update_env DB_CONNECTION=mysql
```

- Migrate The Database.

```bash
python manage.py migrate
```

- Run The Server
```bash
python manage.py runserver
```

- Run the Jobs Schedule.
```bash
python manage.py schedule run < /dev/null
# Or as a process
python manage.py schedule run </dev/null &
```

- Go to `http://127.0.0.1:8000/install` to install the application.

### With Docker

- Get the application code
```bash
git clone https://github.com/Clivern/Kevin.git kevin
cd kevin
cp .env.docker .env
```

- Then run our docker containers
```bash
docker-compose build
docker-compose up -d
```

- Open your browser and access the `http://127.0.0.1:8000/`.

- Also you can add `http://kevin.com` to your `/etc/hosts` file.
```bash
127.0.0.1:8000       kevin.com
```

- To Check our containers, use the following command:
```bash
docker-compose ps
```

- To stop our containers
```bash
docker-compose down
```

### Running on production

Currently kevin is still under development and for sure we will explain how to run it on production after the first release.


### Automated Deployment

Currently we support chef to deploy kevin and even automate your deployment with each release. [Just use this chef cookbook](https://github.com/Clivern/Kevin-Cookbook) and you will amazed with the features it supports.


Misc
====

Changelog
---------
Version 1.0.0:
```
Coming Soon.
```

Acknowledgements
----------------

© 2018, Clivern. Released under [The Apache Software License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt).

**Kevin** is authored and maintained by [@clivern](http://github.com/clivern).
