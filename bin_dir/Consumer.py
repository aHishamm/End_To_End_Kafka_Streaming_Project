#!/usr/bin/env python
import csv
import time 
import sys 
import json 
from confluent_kafka import Consumer, KafkaError, KafkaException
import socket 
import pandas as pd 
import streamlit as st 
st.set_page_config(page_title="stream", layout="wide")
val_list = []
df = pd.DataFrame({'value':val_list})
topic = st.text_input("Enter the topic name")
def process_message(message): 
    t = st.empty() 
    value = message.value() 
    dval = json.loads(value) 
    st.markdown(dval)
    print(dval) 
if st.button('Consume:'):
    conf = {'bootstrap.servers': 'localhost:9092',
                'default.topic.config': {'auto.offset.reset': 'smallest'},
                'group.id': socket.gethostname()}
    kafka_consumer = Consumer(conf) 
    run = True 
    try: 
        while run: 
            kafka_consumer.subscribe([topic]) 
            message = kafka_consumer.poll(1) 
            if message is None: 
                continue 
            if message.error(): 
                if message.error().code() == KafkaError._PARTITION_EOF: 
                    #end of the event 
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %(message.topic(), message.partition(), message.offset()))
                elif message.error().code() == KafkaError.UNKNOWN_TOPIC_OR_PART: 
                    sys.stderr.write('Topic unknown, creating %s topic\n' % (topic))
                elif message.error(): 
                    print('error raised')
                    raise KafkaException(message.error())
            else: 
                process_message(message) 
    except KeyboardInterrupt: 
        pass 
    kafka_consumer.close() 
