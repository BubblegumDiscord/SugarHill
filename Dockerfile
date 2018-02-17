FROM python:3.6-slim-jessie
RUN mkdir /app
WORKDIR /app
ADD ./src/requirements.txt /app
RUN apt-get update
RUN apt-get install -y gcc
RUN pip install -r requirements.txt
ADD ./src /app
CMD python preload.py && python main.py