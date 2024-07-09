import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# App title
st.title('Exploratory Data Analysis')

# File upload
uploaded_file = st.file_uploader("Choose an Excel or CSV file", type=['xlsx', 'csv'])

if uploaded_file:
    # Load the data
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)

    # Display the data
    st.subheader('Data Preview')
    st.write(df.head())

    # Display basic information about the data
    st.subheader('Data Information')
    st.write(df.info())

    # Display summary statistics
    st.subheader('Summary Statistics')
    st.write(df.describe())

    # Display data types
    st.subheader('Data Types')
    st.write(df.dtypes)

    # Plotting section
    st.subheader('Data Visualization')

    # Correlation heatmap
    st.write('Correlation Heatmap')
    plt.figure(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)

    # Pairplot
    st.write('Pairplot')
    st.write(sns.pairplot(df))
    st.pyplot()

    # Select columns for a histogram
    st.write('Histogram')
    column = st.selectbox('Select column for histogram', df.columns)
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    st.pyplot(plt)

    # Select columns for a boxplot
    st.write('Boxplot')
    column = st.selectbox('Select column for boxplot', df.columns, key='boxplot')
    plt.figure(figsize=(10, 6))
    sns.boxplot(df[column])
    st.pyplot(plt)

else:
    st.write('Please upload an Excel or CSV file to begin.')
