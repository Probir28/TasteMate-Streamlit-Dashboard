import streamlit as st
import pandas as pd

st.set_page_config(page_title="TasteMate Dashboard", layout="centered")

st.title("🍽️ TasteMate Streamlit App")
st.write("🚀 Your Streamlit deployment is working!")

# Try loading your CSV (only if it exists)
try:
    df = pd.read_csv("foodapp_survey_synthetic.csv")
    st.success(" Data loaded successfully!")
    st.dataframe(df.head())
except FileNotFoundError:
    st.warning('foodapp_survey_synthetic.csv' not found in repo.")

st.markdown("---")
st.caption("© 2025 TasteMate Cloud Kitchen • Powered by Streamlit")
