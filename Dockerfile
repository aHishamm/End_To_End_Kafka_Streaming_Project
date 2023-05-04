FROM python:3.10 
WORKDIR /home
ADD . /home
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 