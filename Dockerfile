FROM python:3.11.0a6-alpine3.15

WORKDIR /app

COPY . /app

RUN pip install Flask

EXPOSE 3010

CMD ["python3","/app/file.py"]
