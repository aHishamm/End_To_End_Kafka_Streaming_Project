#!/usr/bin/env python
import csv
import time 
import sys 
from argparse import ArgumentParser 
import json 
from dateutil.parser import parse 
from confluent_kafka import Producer
import socket 
import streamlit as st 
from io import StringIO
st.set_page_config(page_title="stream", layout="wide")
topic = st.text_input('Enter the topic name')
def acknowledgement(error, message): 
    if error is not None: 
        print(f"Message failed to deliver message: {str(message.value())}: {str(error)}")  
    else: 
        print(f"Message is produced {str(message.value())}") 
if st.button("Produce: "): 
    parser = ArgumentParser(description=__doc__) 
    parser.add_argument('filename',type=str,help='Name of the .csv file') 
    parser.add_argument('--speed',type=float,default=1,required=False,help='Speed of the time series by a factor')
    args = parser.parse_args() 
    topic_name = topic 
    file_key = args.filename 
    conf = {'bootstrap.servers':"localhost:9092", 'client.id':socket.gethostname()}
    kafka_producer = Producer(conf) 
    read_stream = csv.reader((open(file_key))) 
    #skipping the header from the csv.reader generator 
    next(read_stream) 
    fline = True 
    while True: 
        try: 
            if fline is True: 
                line1 = next(read_stream,None) 
                timestamp, value = line1[0], line1[1]+' '+line1[2] 
                result = {} 
                result[timestamp] = value 
                #dump to json message format 
                json_dump = json.dumps(result) 
                fline = False 
                kafka_producer.produce(topic_name,key=file_key, value = json_dump, callback=acknowledgement) 
            else: 
                line = next(read_stream,None) 
                di1 = parse(timestamp) 
                di2 = parse(line[0]) 
                #calculating the difference 
                difference = ((di2 - di1).total_seconds()) / args.speed 
                time.sleep(difference) 
                timestamp, value = line[0], line1[1]+' '+line1[2]
                result = {} 
                result[timestamp] = value 
                json_dump = json.dumps(result) 
                kafka_producer.produce(topic_name,key=file_key, value=json_dump,callback=acknowledgement)
            kafka_producer.flush() 
        except TypeError: 
            sys.exit() 