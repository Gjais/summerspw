import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt
st.header("       :red[Machine Learning]")
page_choice = st.radio("Select an option for supervised learning",
                       options=['classification',
                                'Regression'])
# st.set_page_config(page_title="machine learning", page_icon="🛠", layout='wide')

st.header(":green[Upload your csv/excel]")
filetype = st.radio("Choose type",options=['CSV','EXCEL'],horizontal=True)
        # uploading section

if filetype =='CSV':
     uploaded_file = st.file_uploader("Upload",type=['csv'])
     if uploaded_file:
                # st.write(type(uploaded_file))
                try:
                    AADI_DATAFRAME = pd.read_csv(uploaded_file)
                    st.session_state['load_data'] = {'data':AADI_DATAFRAME}
                    st.checkbox("Done")
                except Exception as e:
                    st.error("Some error occurred")
else:
            assert filetype=='EXCEL'
            uploaded_file = st.file_uploader("Upload",type=['xlsx','xlx'])
            
            if uploaded_file:
                # Read Excel file
                excel_data = pd.ExcelFile(uploaded_file)

                # Get sheet names
                sheet_names = excel_data.sheet_names
                left,right = st.columns(2)
                chosen_sheet = left.radio("Choose the sheet",
                                        options=sheet_names)
                def create_dataframe(excel,sheet):
                    AADI_DATAFRAME = pd.read_excel(excel,sheet_name=sheet)
                    st.session_state['load_data'] = {'data':AADI_DATAFRAME}
                    
                # right.markdown(":orange[Preview]")
                # right.dataframe(pd.read_excel(excel_data,chosen_sheet).head())
                right.button("Confirm Selection",on_click=create_dataframe,
                            args=[excel_data,chosen_sheet])