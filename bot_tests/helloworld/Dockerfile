FROM python:3.8

WORKDIR /helloworld
COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "./s3test.py"]