FROM python:3.7-slim-buster
WORKDIR /app
ADD . /app/
COPY ./requirements.txt ./app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app


EXPOSE 8080
EXPOSE 8888
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]