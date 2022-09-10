FROM python:3.8

WORKDIR /finished_code

COPY . .
RUN pip install -r requirements.txt

CMD ["python3","./aws_finviz.py"]