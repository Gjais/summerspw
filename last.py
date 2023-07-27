import streamlit as st
import pandas as pg
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model

start="2010-07-20"
end ="2023-07-20"
user_input=st.text_input('Enter stock Ticker','AAPL')
df=data.Datareader(user_input,'yahoo',start,end)
df.head()