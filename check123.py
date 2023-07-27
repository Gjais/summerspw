import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
 
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.svm import SVC
# from xgboost import XGBClassifier
# from sklearn import metrics
 
import warnings
warnings.filterwarnings('ignore')
import os
# import streamlit as st

def main():
    # Custom CSS style to center the content and remove scrollbars
    st.write("""
    <style>
    body {
        margin: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        overflow: hidden;
    }
    .centered {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .main-heading {
        color: green;
    }
    </style>
    """, unsafe_allow_html=True)

    # Load and display the image
    image_path = "Screenshot 2023-07-18 143512.png"  # Replace with the actual path to your image file
    image_name = os.path.basename(image_path)
    st.write('<div class="centered"><img src="{}" alt="{}" width="400"></div>'.format(image_path, image_name), unsafe_allow_html=True)

    # Place the heading inside a div with the "centered" class
    st.write('<div class="centered"><h1>Nivesh Nirvana</h1></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
