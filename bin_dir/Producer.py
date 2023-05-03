import csv
import time 
import sys 
from argparse import ArgumentParser 
import json 
from dateutil.parser import parse 
from confluent_kafka import Producer
import socket 

def acknowledgement(error, message): 
    if error is not None: 
        print(f"Message failed to deliver message: {str(message.value())}: {str(error)}")  
    else: 
        print(f"Message is produced {str(message.value())}") 
parser = ArgumentParser(description=__doc__) 
parser.add_argument('filename',type=str,help='Name of the .csv file') 
parser.add_argument('topic',type=str,help='Name of Kafla topic') 
parser.add_argument('--speed',type=float,default=1,required=False,help='Speed of the time series by a factor')
args = parser.parse_args() 
topic_name = args.topic 
file_key = args.filename 