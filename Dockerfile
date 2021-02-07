FROM python:3.8 as build

# TODO: use flask prod mode
RUN python -m venv work-count
WORKDIR /work-count
COPY server.py lib.py requirements.txt ./
# activate venv
ENV PATH="/work-count/bin:$PATH"
RUN pip install -r requirements.txt

FROM python:3.8-alpine
COPY --from=build /work-count /work-count
COPY --from=build /etc /etc
WORKDIR /word-count
# activate venv
ENV PATH="/work-count/bin:$PATH"

EXPOSE 5000
EXPOSE 8080
# ENV FLASK_APP=server.py
# ENTRYPOINT ["flask", "run"]
# ENTRYPOINT [ "python", "server.py" ]
RUN ls /work-count/bin
# ENTRYPOINT [ "python", "server.py" ]
ENTRYPOINT ["./word-count/bin/uwsgi"]
# CMD ["--http", "127.0.0.1:5000", "--wsgi-file","server.py", "--callable", "app"]