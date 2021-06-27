FROM python:3.8
LABEL maintainer="Emmanuel Dominic <ematembu2@gmail.com>"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
