FROM python:3.8-slim-buster

LABEL maintainer="amir.m.raei@tutanota.com"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]