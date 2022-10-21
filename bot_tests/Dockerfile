#start from base
FROM python:3.8-slim-buster

#OPTIONALLY add the LABEL maintainer for who to contact:

#install system-wide deps for python and ...:
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg

# copy our application code
WORKDIR /usr/src/bot_tests
COPY . .
# WORKDIR /opt/bots

#fetch specific deps
RUN pip3 install -r requirements.txt

#expose port
#EXPOSE 5000

#start app
CMD ["python3", "./bot_test1.py"]