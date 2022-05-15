FROM python:slim

ADD . /nosqlpot

WORKDIR /nosqlpot

RUN pip install -r requirements.txt

CMD ["python3","nosqlpot.py"]
