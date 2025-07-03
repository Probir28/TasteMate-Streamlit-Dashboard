with open(os.path.join(repo_name, 'app.py'), 'w') as app_file:
    app_file.write('''import streamlit as st

st.title("TasteMate Food Delivery Dashboard")

st.sidebar.title("Navigation")
tabs = st.sidebar.radio("Choose Tab", ["Data Visualization", "Classification", "Clustering", "Association Rule Mining", "Regression"])

if tabs == "Data Visualization":
    st.header("Descriptive Insights")
    st.write("Visualize descriptive insights here.")
elif tabs == "Classification":
    st.header("Classification Models")
    st.write("Classification analysis here.")
elif tabs == "Clustering":
    st.header("Clustering Analysis")
    st.write("Clustering insights here.")
elif tabs == "Association Rule Mining":
    st.header("Association Rule Mining")
    st.write("Association rules insights here.")
elif tabs == "Regression":
    st.header("Regression Analysis")
    st.write("Regression insights here.")
''')
