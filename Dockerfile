FROM python:2.7.15-jessie
RUN pip install -r requirements.txt
EXPOSE 5000
WORKDIR /
COPY code.py code.py
ENTRYPOINT FLASK_APP=hello.py flask run