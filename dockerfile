FROM python:3.13

WORKDIR /app
COPY ./requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Запуск миграций и приложения
CMD alembic upgrade head && python -m uvicorn main:app --host 0.0.0.0 --port 8000
