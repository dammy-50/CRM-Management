# WiFi Company CRM Dashboard
Welcome to the WiFi Company CRM Dashboard repository! This Streamlit application provides comprehensive insights and analytics on customer data for our WiFi company. The goal is to help the team understand customer behavior, improve service quality, and reduce churn rates.  https://crm-management-tjbkbp4amqgb3vvjxbwurw.streamlit.app/


## Features

- **Customer Segmentation**: Analyze customer data based on various attributes such as contract type, international plan, and more.
- **Churn Analysis**: Understand the factors contributing to customer churn and identify areas for improvement.
- **Customer Feedback**: Collect and review feedback from customers to enhance service offerings.

## Application Structure

### Home Section

The Home section provides an overview of the application and its features. Users can navigate to other sections from here.

### Analytics Section

The Analytics section allows users to explore detailed analytics and visualizations on customer data. Key features include:

- **Slicers**: Filter data based on account length and international plan.
- **Customer Segmentation by International Plan**: Visualize customer segmentation using a pie chart.
- **Churn Rate by Area Code**: Analyze churn rates by area code using a bar chart.

### Customer Feedback Section

The Customer Feedback section enables users to provide feedback, which can be used to improve services.

## Installation

To run this application, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/wifi-company-crm.git
   ```
2. Navigate to the project directory:
   ```bash
   cd wifi-company-crm
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Data

The application uses a CSV file (`telecom_churn.csv`) containing customer data. Ensure this file is located at the specified path in the `load_data` function.

## Code Overview

### `app.py`

This is the main file of the application. It contains the following sections:

- **Page Configuration**: Sets the page title, icon, and layout.
- **Data Loading**: Loads and caches the customer data from a CSV file.
- **App Layout**: Defines the layout of the app, including the sidebar navigation and different sections (Home, Analytics, Customer Feedback).
- **Home Section**: Displays an overview of the application.
- **Analytics Section**: Provides interactive data slicers and visualizations.
- **Customer Feedback Section**: Collects and displays customer feedback.

## Dependencies

- Streamlit
- Pandas
- Plotly
- PIL

I ensured these dependencies are installed using the `requirements.txt` file.

## Usage

1. **Home**: Get an overview of the app and its features.
2. **Analytics**: Explore detailed analytics and visualizations on customer data.
3. **Customer Feedback**: Provide your feedback to help us improve our services.

## Contributing

I welcome contributions to improve this project. Please fork the repository and submit a pull request with your changes.

