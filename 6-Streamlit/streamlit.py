import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlit")

## create a simple dataframe
df = pd.DataFrame({
    'Number': [1,2,3,4,5],
    'Name': ['Jack', 'Chaudhary', 'Nadeem', 'Chaudhary', 'Chaudhary']
})
st.write("Here is the data frame")
st.write(df)