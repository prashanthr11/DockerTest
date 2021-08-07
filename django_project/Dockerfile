FROM python:3.7-slim-buster

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
ADD . /app/
COPY . /app


EXPOSE 8080
EXPOSE 8888
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]