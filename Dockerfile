FROM python:3.6.13

RUN pip3 install Flask==1.1.2 \
                 hotqueue==0.2.8 \
                 redis==3.5.3

COPY ./source /app/
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["/app/api.py"]

FROM redis:6.2.1

CMD ["redis-server", "/config/redis.conf"]

FROM python:3.6.13

RUN pip3 install hotqueue==0.2.8 \
                 redis==3.5.3

COPY ./source /app/
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["/app/worker.py"]


