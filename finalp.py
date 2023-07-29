import streamlit as st 
import pandas as pd 
import numpy as np
st.set_page_config(page_title="Nivesh Nirvana", page_icon="📈", layout='wide')
import seaborn as sb

import matplotlib.pyplot as plt
import base64


def mains():
    # Ticker with some custom CSS styling
    st.markdown(
        """
        <style>
            /* Ticker CSS */
            .ticker-wrap {
                width: 100%;
                padding: 25px 0;
                overflow: hidden;
                box-sizing: border-box;
                
            }
            
            .ticker {
                display: inline-block;
                white-space: nowrap;
                padding-right: 100%;
                animation: ticker 150s linear infinite;
            }
            
            @keyframes ticker {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Ticker content
    st.markdown(
        """
        <div class="ticker-wrap">
            <div class="ticker">
                

               Action Const	675.50 (+1.21)      BEML 1,805.00 (+1.83)        DB (Int)Stock 24.40 (+1.46)      DCM 82.55 (-1.48)       Mangalam Organ 464.00 (+0.75)      Dynamic Service 37.00(+1.75)      Engineers India 149.00(+7.55)      EID Parry	487.00(+6.30)      Eris Life 758.05(+4.15)      GAIL 116.90(-4.85)      Goodyear 1,435.00(+5.40)      General Insuran 202.20(+3.75)      Godrej Prop 1,650.00(+1.60)      Gujarat Pipavav 123.90(+1.50)      HDFCSML250	111.90(-0.33)      HUDCO 64.85(+2.25)      INOXGREEN 67.45(+3.05)      ISL 66.00(+0.90)      ILandFS 9.30(-0.25)      Dhani Services 39.90(+0.70)      Inox Wind Energ 2,650.00(+48.50)      KEC Intl 648.80(-11.65)      Macrotech Dev	730.00(-8.60)      Mahalaxmi Rub 157.25(+7.45)      Mah Seamless 501.50(+24.25)      Magadh Sugar 487.05(+17.10)      New India Assur 123.70(+0.35)      SDL24BEES 114.94(+0.05)      AUTOBEES	159.50(+1.23)      Country Condos 5.20(+0.45)      ONGC	172.70(+1.70)      Repro India	760.00(+18.80)      Rossell India 448.00(-9.45)      Rategain Travel 446.95(+5.40)      Sirca Paint 368.30(-0.25)	

                
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    mains()

def show_my_profile():
    st.title("My Profile")
    st.write("Please fill in your details below:")

    # Use st.form to create a form for the user to fill in their details
    with st.form(key='profile_form'):
        name = st.text_input("Name:")
        email = st.text_input("Email:")
        address = st.text_area("Address:")
        submit_button = st.form_submit_button(label='Submit')

        # Process the form data after submission
        if submit_button:
            # Do something with the user's details, e.g., store in a database
            # For now, we'll just display a success message
            st.success("Profile details submitted successfully!")


def side():
    # st.title("Nivesh Nirvana")  # Set the title of the page

    # Sidebar options
    st.sidebar.title("Invest ➡️ Grow ➡️ Suceed")
    sidebar_selection = st.sidebar.radio("Menu:", ["Home", "My Profile", "Markets", "Insights", "News", "Personal Finance", "Invest Now","Portfolio","Mutual Funds","International"])   
    if sidebar_selection == "Home":         
        def main():
            # st.title("Image Display and Control")
        
            # Provide the file path of the image on your PC
            image_path = "logo.png"  # Replace this with your image file path
        
            # Read the image as bytes
            image_bytes = read_image_as_bytes(image_path)
        
            
        
                # Apply the size and position adjustments to the image
            image_style = f"width: {562}px; height: {404}px; object-fit: cover; position: relative; top: {0}%; left: {28}%;"
        
                # Encode the image bytes in base64
            encoded_image = base64.b64encode(image_bytes).decode()
        
                # Display the image with the given style and base64 encoding
            st.markdown(f'<img src="data:image/png;base64,{encoded_image}" style="{image_style}" alt="Uploaded Image">', unsafe_allow_html=True)
        
        def read_image_as_bytes(file_path):
            try:
                with open(file_path, "rb") as f:
                    image_bytes = f.read()
                return image_bytes
            except FileNotFoundError:
                st.error("Image file not found. Please provide the correct file path.")
                return None
        
        if __name__ == "__main__":
            main()
        
        import yfinance as yf
        
        from keras.models import load_model
        
        def fetch_company_data(company_name):
            company = yf.Ticker(company_name)
            return company.history(period="3y")
        
        def main():
            st.title("Company Stock Data Viewer")
            # st.write("This app fetches historical stock data for a given company and displays it.")
        
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
        # st.subheader('DATA for last Three years')
        # st.write(df.describe())
        if df is not None:
           st.subheader('Closing Price vs Time chart')
           fig = plt.figure(figsize = (12,6))
           plt.plot(df.Close)
           st.pyplot(fig)
        
        
        
        # st.subheader('Closing Price vs Time chart with 100MA')
        # ma100 = df.Close.rolling(100).mean()
        # fig = plt.figure(figsize = (12,6))
        # plt.plot(ma100)
        # plt.plot(df.Close)
        # st.pyplot(fig)
        
        # st.subheader('Closing Price vs Time chart with 100MA & 200MA')
        # ma100 = df.Close.rolling(100).mean()
        # ma200 = df.Close.rolling(200).mean()
        # fig = plt.figure(figsize = (12,6))
        # plt.plot(ma100,'r')
        # plt.plot(ma200,'g')
        # plt.plot(df.Close,'b')
        # st.pyplot(fig)
        
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
           
           plt.plot(y_test, 'b',label='Original price') 
           plt.plot(y_predicted, 'r',label='predicted price' )
           
           plt.xlabel('Time')
           plt.ylabel('Price')
           
           #
           
           plt.legend()
           
           st.pyplot(fig2)
        
        
        
        
      
        
        
        
        def main():
            # Custom CSS for the two-column layout
            st.markdown(
                """
                <style>
                    /* Two-column layout CSS */
                    .container {
                        display: flex;
                        width: 100%;
                    }
                    
                    .main-content {
                        flex: 1;
                        padding: 20px;
                    }
                    
                    .side-content {
                        flex: 0 0 25%; /* Set the side content to be 25% of the width */
                        padding: 20px;
                        background-color: #f1f1f1; /* You can change the background color here */
                    }
                </style>
                """,
                unsafe_allow_html=True
            )
        
            # Main content
            st.markdown('<h1 style="text-align: right; color: red;">Market Action BSE</h1>', unsafe_allow_html=True)
            st.markdown('<h1 style="text-align: left; color: blue;">Top News</h1>', unsafe_allow_html=True)
            
            # st.markdown("#L&T Q1 Results: Net profit spikes 46.5% to Rs 2,493 crore, beats estimates")
        
            # Two-column layout
            st.markdown(
                """
                <div class="container">
                    <div class="main-content">
                      <h2></h2>
                        <ul>
                            <li>IMF raises India's FY24 GDP growth forecast by 20 bps to 6.1%</li>
                            <li>Tata Motors proposes to convert DVR shares to ordinary shares.</li>
                            <li>L&T Q1 Results: Net profit spikes 46.5% to Rs 2,493 crore, beats estimates</li>
                            <li>ONDC is going global, eyes B2B exports to UAE, Singapore by year-end</li>
                        </ul>
                    </div>   
                    
                    
                    
                    
                      Top Gainers
                        HINDALCO   449.85 (📈4.09%)     
                        TATASTEEL  119.78 (📈3.25%)  
                        JSWSTELL   800.55 (📈3.21%)        
                        NTPC       300.66 (📈2.11%)
                        ULTRACEMCO 200.88 (📈1.85%)
                      
                      
                     Top Losers
                        ASIANPAINT  3400.43 (📉4.40%)
                        ITC         462.30  (📉1.92%)
                        L&T         462.30  (📉1.70%)
                        BRITANNIA   4885.60 (📉1.68%)
                        INDUSINDBK  1415.45 (📉1.41%)
                     
          
                </div>
                """,
                unsafe_allow_html=True
            )
        
        if __name__ == '__main__':
            main()
            st.markdown('<h1 style="text-align: left; color: Blue;">SENSEX Prediction</h1>', unsafe_allow_html=True)
        
            st.markdown(
                """
                <div class="container">
                    <div class="main-content">
                      <li>SENSEX (66,356) Sensex is currently in negative trend. If you are holding short positions then continue to hold with daily closing stoploss of 66,937. Fresh long positions can be initiated if Sensex closes above 66,937 levels.</li>
                      <li>SENSEX Support 66,169 - 65,983 - 65,787</li>
                      <li>SENSEX Resistance 66,551 - 66,746 - 66,932</li>
                      <li>SENSEX Tentative Range ( Accuracy 92% )</li> 
                    </div>   
                    
          
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown('<h1 style="text-align: left; color: Blue;">NIFTY Prediction</h1>', unsafe_allow_html=True)
        
            st.markdown(
                """
                <div class="container">
                    <div class="main-content">
                      <li>NIFTY (19,681) Nifty is currently in negative trend. If you are holding short positions then continue to hold with daily closing stoploss of 19,833. Fresh long positions can be initiated if Nifty closes above 19,833 levels.</li>
                      <li>NIFTY Support 19,621 - 19,562 - 19,508</li>
                      <li>NIFTY Resistance 19,735 - 19,789 - 19,848</li>
                      <li>NIFTY Tentative Range ( Accuracy 92% )</li> 
                    </div>   
                    
          
                </div>
                """,
                unsafe_allow_html=True
            )
            st.markdown('<h1 style="text-align: left; color: Blue;">BANKNIFTY Prediction</h1>', unsafe_allow_html=True)
            st.markdown(
                """
                <div class="container">
                    <div class="main-content">
                      <li>BANKNIFTY (45,845) Banknifty is currently in positive trend. If you are holding long positions then continue to hold with daily closing stoploss of 45,662 Fresh short positions can be initiated if Banknifty closes below 45,662 levels</li>
                      <li>BANKNIFTY Support 45,593 - 45,341 - 45,060</li>
                      <li>BANKNIFTY Resistance 46,126 - 46,408 - 46,660</li>
                      <li>BANKNIFTY Tentative Range ( Accuracy 92% )</li> 
                    </div>   
                    
          
                </div>
                """,
                unsafe_allow_html=True
            )
            #st.markdown('<h1 style="text-align: center; color: orange;">Get Daily Prediction & Stocks Tips On Your Mobile</h1>', unsafe_allow_html=True)
            # st.markdown('<h1 style="text-align: left; color: blue;">Top News</h1>', unsafe_allow_html=True)
            
            # st.markdown("#L&T Q1 Results: Net profit spikes 46.5% to Rs 2,493 crore, beats estimates")
        
            # Two-column layout
        def main():
            # Main content
            #st.markdown('<h1 style="text-align: center; color: green;">Get Daily Prediction & Stocks Tips</h1>', unsafe_allow_html=True)
        
            # Form container
            st.markdown("## :violet[Get Daily Prediction & Stocks Tips]")
            
            # User Inputs
            name = st.text_input("Name")
            email = st.text_input("Email")
            mobile = st.text_input("Mobile Number")
        
            # Checkbox for Terms and Conditions
            terms_accepted = st.checkbox("I agree to the Terms and Conditions")
        
            # Submit button
            if st.button("Submit"):
                if terms_accepted:
                    # Perform actions with the form data
                    st.success("Welcome To Nivesh Nirvana!!!")
                else:
                    st.error("Please agree to the Terms and Conditions.")
        
        if __name__ == '__main__':
                    main()
                
        
        # Function to create social media buttons


        # Function to create social media buttons
        def social_media_links():
            st.markdown("## :red[ Connect with Us]:")
            
            # Replace the URLs with your actual social media profile URLs
            twitter_url = "https://twitter.com/GauravJ69899269"
            linkedin_url = "https://www.linkedin.com/in/gaurav-jaiswal-9788a6256/"
            github_url = "https://github.com/Gjais"
            
            # Create buttons with social media icons and link them to your profiles
            col1, col2, col3 = st.columns(3)
        
            
            st.markdown(f'[![Twitter](https://img.icons8.com/fluent/48/000000/twitter.png)]({twitter_url})', unsafe_allow_html=True)
        
            
            st.markdown(f'[![LinkedIn](https://img.icons8.com/fluent/48/000000/linkedin.png)]({linkedin_url})', unsafe_allow_html=True)
        
            
            st.markdown(f'[![GitHub](https://img.icons8.com/fluent/48/000000/github.png)]({github_url})', unsafe_allow_html=True)
        
        def main():
            # st.title("My Personal Website")
            # st.write("Welcome to my personal website! Feel free to explore the content.")
            
            # # Add other sections or content as needed
            # st.header("About Me")
            # st.write("I am a software developer passionate about AI and web development.")
        
            # Adding social media links
            social_media_links()
        
        if __name__ == "__main__":
            main()

  
        def disclaimer():
            st.write("Disclaimer:")
            st.write("This application is for educational purposes only and does not constitute financial advice. "
                     "The stock data displayed here may not be accurate or up-to-date. "
                     "Investing in the stock market involves risks, and past performance is not indicative of future results. "
                     "Before making any investment decisions, seek advice from a qualified financial professional.")
        
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
        
        
            # Display the disclaimer
            disclaimer()
            
    
    elif sidebar_selection == "My Profile":
        # Show the "My Profile" page when the user clicks on "My Profile" in the sidebar
        show_my_profile()
    elif sidebar_selection == "Markets":
        # Add content for Tab 1
        st.header("T")
        st.write("This is Markets. You can customize the content here.")
    elif sidebar_selection == "Insights":
        # Add content for Insights
        st.header("Insights")
        st.write("This is Insights. You can customize the content here.")
    elif sidebar_selection == "News":
        # Add content for News
        st.header("News")
        st.write("This is News. You can customize the content here.")
    elif sidebar_selection == "Personal Finance":
        # Add content for Personal Finance
        st.header("Personal Finance")
        st.write("This is Personal Finance. You can customize the content here.")
    elif sidebar_selection == "Invest Now":
        # Add content for Tab 5
        st.header("Invest Now")
        st.write("This is Invest Now You can customize the content here.")
    elif sidebar_selection == "Portfolio":
        # Add content for Tab 5
        st.header("Tab 5")
        st.write("This is Invest Now You can customize the content here.")
    elif sidebar_selection == "Mutual funds":
        # Add content for Tab 5
        st.header("International")
        st.write("This is Invest Now You can customize the content here.")  
        

        # Define a function to display articles about mutual funds
        def display_article(title, content, image_url):
            st.subheader(title)
            st.image(image_url, use_column_width=True)
            st.write(content)
        
        # Main content of the mutual funds section
        def mutual_funds_section():
            st.title("Mutual Funds")
        
           
      
if __name__ == "__main__":
    side()






#   with st.sidebar:
#             st.markdown("My Profile")
#             st.markdown("Markets")
#             st.markdown("Insight")
#             st.markdown("News")
#             st.markdown("Portfolio")
#             st.markdown("Mutual Funds")
#             st.markdown("Personal Finance")
#             st.markdown("Forum")
#             st.markdown("Invest Now")
#             st.markdown("International")
        