FROM python:3.8-slim
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
RUN python manage.py migrate
RUN python manage.py collectstatic
ENV PORT 8080
CMD gunicorn --bind :$PORT --workers 3 project_manager.wsgi:application

