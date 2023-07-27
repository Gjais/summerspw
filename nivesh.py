import yfinance as yf
import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



import streamlit as st
import yfinance as yf
import pandas as pd
from keras.models import load_model

def fetch_company_data(company_name):
    company = yf.Ticker(company_name)
    return company.history(period="3y")

def main():
    st.title("Company Stock Data Viewer")
    st.write("This app fetches historical stock data for a given company and displays it.")

    # Input for the user to enter the company name
    company_name = st.text_input("Enter the company name (e.g., AAPL for Apple Inc.):")

    if company_name:
        try:
            # Fetch data from yfinance for the given company
            data = fetch_company_data(company_name)
            if data.empty:
                st.warning("No data found for the provided company name.")
            else:
                # Display the data in a table
                st.write(f"Historical Data for {company_name.upper()}:")
                st.dataframe(data)

                # Return the DataFrame for further use
                return data
        except Exception as e:
            st.error("An error occurred while fetching data. Please check the company name and try again.")

if __name__ == "__main__":
    # Store the returned DataFrame in a variable 'df'
    df = main()

    # Now you can use 'df' for further data processing or analysis if needed
    # For example, you can print the first few rows of 'df'
    if df is not None:
        print(df.head())
st.subheader('DATA for last 3 years')
st.write(df.describe())
st.subheader('Closing Price vs Time chart')
fig = plt.figure(figsize = (12,6))
plt.plot(df.Close)
st.pyplot(fig)



st.subheader('Closing Price vs Time chart with 100MA')
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100)
plt.plot(df.Close)
st.pyplot(fig)

st.subheader('Closing Price vs Time chart with 100MA & 200MA')
ma100 = df.Close.rolling(100).mean()
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize = (12,6))
plt.plot(ma100,'r')
plt.plot(ma200,'g')
plt.plot(df.Close,'b')
st.pyplot(fig)

data_training=pd.DataFrame(df['Close'][0:int(len(df)*0.70)])
data_testing=pd.DataFrame(df['Close'][int(len(df)*0.70):int(len(df))])

from sklearn.preprocessing import MinMaxScaler

scaler=MinMaxScaler(feature_range=(0,1))
data_training_array=scaler.fit_transform(data_training)

x_train=[]
y_train=[]

for i in range(100,data_training_array.shape[0]):
    x_train.append(data_training_array[i-100:i])
    y_train.append(data_training_array[i,0])
    
x_train,y_train=np.array(x_train),np.array(y_train)    

# from keras.layers import Dense,Dropout,LSTM
# from keras.models import Sequential

# model=Sequential()
# model.add(LSTM(units=50 ,activation= 'relu' , return_sequences=True ,input_shape = (x_train.shape[1],1)))
# model.add(Dropout(0.2))
# model.add(LSTM(units=60 ,activation= 'relu' , return_sequences=True ))
# model.add(Dropout(0.3))
# model.add(LSTM(units=80 ,activation= 'relu' , return_sequences=True ))
# model.add(Dropout(0.4))
# model.add(LSTM(units=50 ,activation= 'relu'  ))
# model.add(Dropout(0.5))

# model.add(Dense(units=1))

# model.compile(optimizer='adam',loss='mean_squared_error')
# model.fit(x_train,y_train,epochs=50)

# model.save('keras_model.h5')

# load my model
model= load_model('keras_model.h5')
past_100_days=data_training.tail(100)




# final_df = past_100_days.append(data_testing, ignore_index=True)
final_df = pd.concat([past_100_days, data_testing], ignore_index=True)
input_data = scaler.fit_transform(final_df)

x_test = []

y_test = []

for i in range(100, input_data.shape[0]):

 x_test.append(input_data[i-100: i])
 y_test.append(input_data[i, 0])
 
x_test, y_test = np.array(x_test), np.array(y_test) 
y_predicted = model.predict(x_test)
scaler=scaler.scale_

scale_factor = 1/scaler[0]
y_predicted = y_predicted*scale_factor
y_test = y_test*scale_factor

st.subheader('Predictions vs Original')

fig2= plt.figure(figsize=(12,6))

plt.plot(y_test, 'b') 
plt.plot(y_predicted, 'r' )

plt.xlabel('Time')
plt.ylabel('Price')

#

plt.legend()

st.pyplot(fig2)