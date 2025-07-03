import streamlit as st
import pandas as pd

# App Title
st.title("🍽️ TasteMate Food Delivery Dashboard")

# Load dataset
@st.cache_data
def load_data():
    data = pd.read_csv("foodapp_survey_synthetic.csv")
    return data

df = load_data()

# Sidebar navigation
st.sidebar.title("Navigation")
tabs = st.sidebar.radio("Choose Tab", ["Data Visualization", "Classification", "Clustering", "Association Rule Mining", "Regression"])

# Tabs content
if tabs == "Data Visualization":
    st.header("📊 Descriptive Insights")
    st.write(df.head())

elif tabs == "Classification":
    st.header("📌 Classification Analysis")
    st.write("Classification analysis will be shown here.")

elif tabs == "Clustering":
    st.header("📍 Clustering Analysis")
    st.write("Clustering insights will be shown here.")

elif tabs == "Association Rule Mining":
    st.header("🔗 Association Rule Mining")
    st.write("Association rule mining insights will be shown here.")

elif tabs == "Regression":
    st.header("📈 Regression Analysis")
    st.write("Regression analysis will be shown here.")

df = pd.read_csv("foodapp_survey_synthetic.csv")

