FROM python:3.7

RUN apt update

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "init.py"]

#ENTRYPOINT ["python", "./genre_classifier.py"]