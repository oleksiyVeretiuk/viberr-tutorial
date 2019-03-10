FROM python:3.6.8-stretch


RUN apt install git

RUN git clone https://github.com/oleksiyVeretiuk/viberr-tutorial

WORKDIR viberr-tutorial

RUN pip install -r requirements.txt

RUN git pull origin master


EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]