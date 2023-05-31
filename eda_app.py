# Framework Library
import streamlit as st

# Supporting Library
# import os

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


data = r"C:\Users\Windows\Downloads\DataSets-main (8)\DataSets-main\wine.csv"
data_cleanded = r"C:\Users\Windows\Downloads\DataSets-main (8)\DataSets-main\wine.csv"
data_freq = r"C:\Users\Windows\Downloads\DataSets-main (8)\DataSets-main\wine.csv"


# def main():
#     run_eda_app()

# if _name_ == "_main_":
#     main()


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
            
        with st.expander("	fixed acidity Distribution"):
            st.dataframe(df['fixed acidity'].value_counts())
            
        with st.expander("quality Distribution"):
            st.dataframe(df['quality'].value_counts())

    else:
        st.subheader("Plot")
        
        col1,col2 = st.columns([2,1])
        
        

        with col1:
          with st.expander("Distribution of fixed acidity"):
            fig = plt.figure()
            sns.countplot(x='fixed acidity', data=df)
            st.pyplot(fig)

            gen_df = df['fixed acidity'].value_counts().to_frame()
            gen_df = gen_df.reset_index()
            gen_df.columns = ['fixed acidity Type', 'Counts']

            p1 = px.pie(gen_df, names='fixed acidity Type', values='Counts')
            st.plotly_chart(p1, use_container_width=True)

        with st.expander("Dist Plot of quality"):
            fig = plt.figure()
            sns.countplot(x='quality', data=df)
            st.pyplot(fig)

    # Column 2
    col2 = st.sidebar

    with col2:
        with st.expander("fixed acidity Distribution"):
            st.dataframe(df['fixed acidity'].value_counts())

        with st.expander("quality Distribution"):
            st.dataframe(df['quality'].value_counts())

    # Additional Plots
    with st.expander("Outlier Detection Plot"):
        fig = plt.figure()
        sns.boxplot(df['fixed acidity'])
        st.pyplot(fig)

        p3 = px.box(df, x='fixed acidity', color='quality')
        st.plotly_chart(p3, use_container_width=True)

    with st.expander("Correlation Plot"):
        corr_matrix = df.corr()
        fig = plt.figure(figsize=(20, 10))
        sns.heatmap(corr_matrix, annot=True)
        st.pyplot(fig)

        p4 = px.imshow(corr_matrix)
        st.plotly_chart(p4)
        
    
if __name__ == "__main__":
    run_eda_app()