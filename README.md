# Binance_API_Kafka_Streaming_Project
This is a simulation project that utilized the Kafka event streaming platform. 

I pull time-series cryptocurrency data from the Binance API and stream the data line by line via Kafka, a producer and consumer applications are written for the simulation purposes. 

### Implementation Steps 
1. Docker Desktop and Docker Compose has to be installed on the Machine to run kafka and zookeeper. 
2. Conda has to be installed to create a venv (install the provided requirements.txt)
```bash
conda create -n kafka_stream python=3.10 
conda activate kafka_stream 
pip install -r requirements.txt
```
3. Run a multi-container app using Docker Compose.
```bash
docker compose up --build 
```
4. In a separate terminal window, run the **Producer.py** application (use **generate.py** to pull up to date information from the Binance API). 
```bash
streamlit run bin_dir/Producer.py data_dir/binance.csv
```
5. In a separate terminal window, run the **Consumer.py** application. 
```bash
streamlit run bin_dir/Consumer.py
```
6. To shutdown, run the following: 
```bash
docker compose down
```