FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD requirements.txt /app/
RUN pip install -r requirements.txt

COPY ./docker-entrypoint.sh ./docker-entrypoint.sh
RUN chmod +x docker-entrypoint.sh
COPY . .

EXPOSE 8000

ENTRYPOINT [".  /docker-entrypoint.sh"]