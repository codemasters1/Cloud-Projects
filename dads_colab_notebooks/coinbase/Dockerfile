FROM python:3.8

WORKDIR /coinbase

COPY . .
RUN pip install -r requirements.txt

CMD ["python3", "./coinbase_coins_list.py"]