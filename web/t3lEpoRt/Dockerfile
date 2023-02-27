FROM python:3.8-slim-buster

COPY challenge /challenge/

WORKDIR /challenge

RUN pip3 install flask

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
