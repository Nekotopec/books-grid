FROM python:3.7.9-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /book_store
RUN mkdir /logs
RUN cat > /logs/gunicorn.log
WORKDIR /book_store/
RUN cat > __init__.py
COPY requirements.txt /book_store/
RUN pwd
RUN pip install -r requirements.txt
COPY ./book_store ./
COPY docker/backend/entrypoint.sh /
RUN chmod +x /entrypoint.sh
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py docker_init_admin
#RUN pytest -x -v