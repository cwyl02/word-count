# FROM python:3.8 as build
FROM python:3.8-alpine3.11

RUN python -m venv work-count
WORKDIR /work-count
# activate venv
ENV PATH="/work-count/bin:$PATH"
COPY server.py lib.py requirements.txt uwsgi_static.ini ./

# uh!
RUN apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers\
    && pip install -r requirements.txt \
    && apk del .build-deps gcc libc-dev linux-headers

RUN addgroup -S uwsgi &&  adduser -S uwsgi -G uwsgi
RUN chown -R uwsgi:uwsgi /work-count
EXPOSE 5000

ENTRYPOINT ["uwsgi", "--ini", "uwsgi_static.ini"]
# ENTRYPOINT ["./word-count/bin/uwsgi"]
# CMD ["--http", "127.0.0.1:5000", "--wsgi-file","server.py", "--callable", "app"]