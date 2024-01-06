import pandas as pd
import streamlit as st
import pickle

# Load the car data
try:
    car_data = pd.read_pickle('deploy_car_df.pickle')
except Exception as e:
    st.error(f"Error loading car data: {e}")
    st.stop()

# Load the model
try:
    with open('deploy_car.pickle', 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Streamlit app
st.title("Used Car Worth Estimators")

# Rest of your code...
