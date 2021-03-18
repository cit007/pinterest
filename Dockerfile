FROM python:3.9.2

WORKDIR /home/

RUN git clone https://github.com/cit007/pinterest.git

WORKDIR /home/pinterest/

RUN pip install gunicorn

RUN pip install -r requirements.txt

RUN echo "xxx" > .env

RUN python manage.py migrate

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "pinterest.wsgi", "--bind", "0.0.0.0:8000"]