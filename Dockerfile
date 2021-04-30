FROM python:3.9

RUN apt-get update && apt-get install -y vim

RUN pip install flask redis hotqueue ipython
RUN mkdir /app

RUN touch /foo
COPY source /app

WORKDIR /app

ENTRYPOINT ["python"]

