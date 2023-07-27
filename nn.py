import streamlit as st 
import pandas as pd 
import numpy as np
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import requests
st.header("Nivesh Nirvana")
 # Set your Alpha Vantage API key
api_key = '2K7EWE1RDJ0MR4M6'

# Define the function to retrieve stock market data
def get_stock_data(symbol, start_date, end_date):
    base_url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': symbol,
        'outputsize': 'full',
        'apikey': api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Extract the daily stock prices from the response
    daily_data = data['Time Series (Daily)']
    
    # Convert the data into a pandas DataFrame
    df = pd.DataFrame.from_dict(daily_data, orient='index')
    df.index = pd.to_datetime(df.index)
    df = df[(df.index >= start_date) & (df.index <= end_date)]
    df = df.astype(float)
    
    return df

# Define the start and end dates
start_date = '2023-07-17'
end_date = '2023-01-01'

# Retrieve the stock market data for AAPL
df = get_stock_data('AAPL', start_date, end_date)

# Display the table data as a string
print(df.head().to_string(index=True))