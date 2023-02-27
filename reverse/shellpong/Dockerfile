FROM python:3.10-alpine

RUN apk update && \
    apk add socat

COPY app /app

WORKDIR /app

RUN pip install -r requirements.txt

RUN chmod +x app.py 

EXPOSE 1337

ENTRYPOINT ["python"]

CMD ["app.py"]
