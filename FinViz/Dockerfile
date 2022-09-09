FROM python:3.8

WORKDIR ./FinViz

COPY FinViz/requirements.txt ./
RUN pip install --no-=cache-dir -r requirements.txt

COPY ./FinViz ./FinViz

CMD python FinViz/aws_finviz.py