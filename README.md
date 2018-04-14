# Kevin
Tool to Inspect HTTP Requests & Build Custom Endpoints.

[![Build Status](https://travis-ci.org/Clivern/Kevin.svg?branch=master)](https://travis-ci.org/Clivern/Kevin)

Installation
------------

In order to run this app do the following:

### Default Install

```bash
#
```

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


Acknowledgements
----------------

© 2018, Clivern. Released under [The Apache Software License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.txt).

**Kevin** is authored and maintained by [@clivern](http://github.com/clivern).