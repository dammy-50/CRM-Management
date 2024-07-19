import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import requests
from io import BytesIO

# Set the page configuration
st.set_page_config(page_title="WiFi Company CRM", page_icon=":satellite:", layout="wide")

# Load and cache data
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/dammy-50/CRM-Management/main/telecom_churn.csv"
    data = pd.read_csv(url)
    return data

data = load_data()

# Image URLs
logo_url = "https://raw.githubusercontent.com/dammy-50/CRM-Management/main/wifi.jpeg"
background_url = "https://raw.githubusercontent.com/dammy-50/CRM-Management/main/homepage.jpeg"

# Load images
def load_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

# App layout
def main():
    # Sidebar
    st.sidebar.image(load_image(logo_url), use_column_width=True)
    st.sidebar.title("WiFi CRM Dashboard")
    st.sidebar.markdown("### Navigation")
    nav = st.sidebar.radio("Navigation", ["Home", "Analytics", "Customer Feedback"])

    if nav == "Home":
        home_app()
    elif nav == "Analytics":
        analytics_app()
    elif nav == "Customer Feedback":
        feedback_app()

# Home section
def home_app():
    st.image(load_image(background_url), use_column_width=True)
    st.title("Welcome to the WiFi Company CRM 📡")
    st.markdown("""
        ### Overview
        This application is designed to provide comprehensive insights and analytics on customer data for our WiFi company. The goal is to help our team understand customer behavior, improve service quality, and reduce churn rates.

        ### Features
        - **Customer Segmentation**: Analyze customer data based on various attributes such as contract type, international plan, and more.
        - **Churn Analysis**: Understand the factors contributing to customer churn and identify areas for improvement.
        - **Customer Feedback**: Collect and review feedback from customers to enhance service offerings.

        ### How to Use
        - **Home**: Get an overview of the app and its features.
        - **Analytics**: Explore detailed analytics and visualizations on customer data.
        - **Customer Feedback**: Provide your feedback to help us improve our services.

        We hope you find this application useful and insightful. Enjoy exploring! 😊
    """)

# Analytics section
def analytics_app():
    st.title("Customer Data Analytics 📊")

    # Slicers
    account_length = st.slider("Select Account Length", min_value=int(data['account length'].min()), max_value=int(data['account length'].max()), value=(int(data['account length'].min()), int(data['account length'].max())))
    international_plan = st.selectbox("Select International Plan", options=data['international plan'].unique())
    
    # Filter data based on slicers
    filtered_data = data[(data['account length'] >= account_length[0]) & (data['account length'] <= account_length[1]) & (data['international plan'] == international_plan)]
    
    # Data visualization
    st.subheader("Customer Segmentation by International Plan")
    segmentation_fig = px.pie(filtered_data, names='international plan', title='Customer Segmentation by International Plan')
    st.plotly_chart(segmentation_fig, use_container_width=True)

    st.subheader("Churn Rate by Area Code")
    churn_fig = px.bar(filtered_data, x='area code', y='churn', color='churn', title='Churn Rate by Area Code', barmode='group')
    st.plotly_chart(churn_fig, use_container_width=True)

# Customer Feedback section
def feedback_app():
    st.title("Customer Feedback 💬")
    st.markdown("### Please provide your feedback below:")
    feedback = st.text_area("Your Feedback", height=200)
    if st.button("Submit"):
        st.success("Thank you for your feedback! 😊")

# Run the app
if __name__ == "__main__":
    main()
