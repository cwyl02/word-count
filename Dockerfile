FROM python:3.8-alpine

# TODO: use flask prod mode
RUN python -m venv work-count
WORKDIR /work-count
COPY server.py lib.py requirements.txt ./
RUN ls
RUN pip install -r requirements.txt

ENV FLASK_APP=server.py
ENTRYPOINT [ "flask", "run" ]