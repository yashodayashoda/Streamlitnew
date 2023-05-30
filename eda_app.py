# Framework Library
import streamlit as st

# Supporting Library
import os

# Core Libraries
import pandas as pd
import numpy as np

# Visualization Libraries
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# Fxns

def load_data(data):
    df = pd.read_csv(data)
    return df

# Paths


data = r"C:\Users\Windows\Downloads\Project_Streamlit-main\Project_Streamlit-main\data\diabetes_data_upload.csv"

data_cleanded = r"C:\Users\Windows\Downloads\Project_Streamlit-main\Project_Streamlit-main\data\diabetes_data_upload_clean.csv"

data_freq = r"C:\Users\Windows\Downloads\Project_Streamlit-main\Project_Streamlit-main\data\freqdist_of_age_data.csv"

def run_eda_app():    
    st.header("EDA")
    
    sub = ["Descriptive",'Plot']
    submenu = st.sidebar.selectbox("Submenu",sub)
    
    df = load_data(data)
    df_encoded = load_data(data_cleanded)
    freq_df = load_data(data_freq)
    
    if submenu == 'Descriptive':
        st.subheader("Descriptive")
        
        st.dataframe(df)
        
        with st.expander("Descriptive Summary"):
            st.dataframe(df_encoded.describe())
        
        with st.expander("Data Types Summary"):
            st.dataframe(df.dtypes)
            
        with st.expander("Gender Distribution"):
            st.dataframe(df['Gender'].value_counts())
            
        with st.expander("Class Distribution"):
            st.dataframe(df['class'].value_counts())

        with st.expander("Class Distribution"):
            st.dataframe(df.describe().T)
               

    else:
        st.subheader("Plot")
        
        col1,col2 = st.columns([2,1])
        
        with col1:
            
            with st.expander("Distribution of Gender"):
                fig = plt.figure()
                sns.countplot(x='Gender', data = df)
                st.pyplot(fig)
                
                gen_df = df['Gender'].value_counts().to_frame()
                gen_df = gen_df.reset_index()
                gen_df.columns = ['Gender Type', 'Counts']
                
                p1 = px.pie(gen_df, names='Gender Type', values='Counts')
                st.plotly_chart(p1, use_container_width=True)
            
            with st.expander("Dist Plot of Class"):
                fig = plt.figure()
                sns.countplot(x='class', data=df)
                st.pyplot(fig)
        
        with col2:
            
            with st.expander("Gender Distribution"):
                st.dataframe(df['Gender'].value_counts())   
                
            with st.expander("Class Distribution"):
                st.dataframe(df['class'].value_counts())
                
        with st.expander("Frequency Dist Plot of Age"):
            p2 = px.bar(freq_df, x='Age', y='count')
            st.plotly_chart(p2, use_container_width=True)
            
        with st.expander("Outlier Detection Plot"):
            fig = plt.figure()
            sns.boxplot(df['Age'])
            st.pyplot(fig)
            
            p3 = px.box(df, x='Age', color='Gender')
            st.plotly_chart(p3, use_container_width=True)
            
        with st.expander("Correlation Plot"):
            corr_matrix = df_encoded.corr()
            fig = plt.figure(figsize=(20, 10))
            sns.heatmap(corr_matrix, annot=True)
            st.pyplot(fig)
            
            p4 = px.imshow(corr_matrix )
            st.plotly_chart(p4)

        
    
if __name__ == "__main__":
    run_eda_app()