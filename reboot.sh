#!/bin/bash

docker pull python:3.10-slim
docker pull selenium/standalone-firefox:4.16.1-20231219

docker network create selenium-host

(docker compose up --exit-code-from=python-app && docker compose down --volumes && docker network rm selenium-host) &



# reference:
# https://github.com/SeleniumHQ/docker-selenium#quick-start
# https://hub.docker.com/_/python
