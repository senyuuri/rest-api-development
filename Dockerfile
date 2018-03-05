FROM python:3.6
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD . /app
RUN chmod +x wait-for-it.sh
RUN pip install -r requirements.txt