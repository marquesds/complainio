# complainio
Service to register and retrieve complains.

[![Build Status](https://travis-ci.org/marquesds/complainio.svg)](https://travis-ci.org/marquesds/complainio)
[![Coverage Status](https://coveralls.io/repos/github/marquesds/complainio/badge.svg?branch=master)](https://coveralls.io/github/marquesds/complainio?branch=master)

![Complain](resources/images/complain.jpg)

## Documentation

You can see how to use complainio's API [here](docs/complain.md). If you use Postman, you can import all requests [here](resources/postman/complainio.postman_collection.json).

## Install and Run

    $ docker-compose up -d

## Get API Key

	$ docker ps
	$ docker exec -it your_docker_container_id /bin/bash
	$ cd usr/complainio/
	$ source .venv/bin/activate
	$ python manage.py generate_api_key -u your_user

## Run Unit Tests

	$ make test

## Generate Coverage Report

	$ make coverage

## Generate Vulnerabilities Report

	$ make bandit
