#start from base
FROM python:3.8-slim-buster

#install system-wide deps for python and ...:
# RUN apt-get -yqq update
# RUN apt-get -yqq install python3-pip python3-dev curl gnupg

# copy our application code
WORKDIR /bot_tests/finished_tiktok
COPY . .

#fetch specific deps
RUN pip3 install -r requirements.txt

#start app
CMD ["python3", "./bot_test1.py"]FinViz/old code