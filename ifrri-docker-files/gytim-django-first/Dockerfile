FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DJANGO_PROJECT "./newsite"

RUN mkdir -p /src/newsite
COPY ${DJANGO_PROJECT} /src/newsite
RUN chmod 0777 /src/newsite/create_base.sh

WORKDIR /src/newsite
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    postgresql-client


    
CMD cd /src/newsite \
    && gunicorn --bind 0.0.0.0:8000 newsite.wsgi:application
