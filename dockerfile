FROM python:3.13

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


