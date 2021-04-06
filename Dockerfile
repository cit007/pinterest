FROM python:3.9.2

WORKDIR /home/

RUN echo "delete cache for deploy in prod"

RUN git clone https://github.com/cit007/pinterest.git

WORKDIR /home/pinterest/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

# RUN python manage.py migrate

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]
CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=pragmatic.settings.prod && python manage.py migrate --settings=pragmatic.settings.prod && gunicorn pragmatic.wsgi --env DJANGO_SETTINGS_MODULE=pragmatic.settings.prod --bind 0.0.0.0:8000"]