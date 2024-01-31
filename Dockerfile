#docker remote os
FROM python:3.10-buster

# 
RUN apt update 


COPY ./requirements.txt /src/usr


RUN pip install --upgrade pip


RUN pip install -r /src/usr/requirements.txt


RUN pip install gunicorn

COPY . /src/usr/

WORKDIR /src/usr

EXPOSE 5001

RUN chmod 777 ./entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]









