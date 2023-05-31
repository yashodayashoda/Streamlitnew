import streamlit as st
import joblib
import os
import pandas as pd
import numpy as np

attrib_info = """
Attribute Information:\n
Fixed Acidity;\n
Volatile Acidity;\n
Citric Acid;\n
Residual Sugar;\n
Chlorides;\n
Free Sulfur Dioxide;\n
Total Sulfur Dioxide;\n
Density;\n
pH;\n
Sulphates;\n
Alcohol;\n
Quality.
"""

label_dict = {"No": 0, "Yes": 1}
gender_map = {"Female": 0, "Male": 1}
target_label_map = {"Negative": 0, "Positive": 1}

# Functions

def get_fvalue(val):
    feature_dict = {"No": 0, "Yes": 1}
    for key, value in feature_dict.items():
        if val == key:
            return value

def get_value(val):
    gender_map = {"Female": 0, "Male": 1}
    for key, value in gender_map.items():
        if val == key:
            return value

def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model

# Main ML APP Function

def run_ml_app():

    st.subheader("ML Prediction")

    with st.expander("Attribute Info"):
        st.write(attrib_info)

    # Layout

    col1, col2 = st.columns(2)

    with col1:
        fixed_acidity = st.number_input("Fixed Acidity")
        volatile_acidity = st.number_input("Volatile Acidity")
        citric_acid = st.number_input("Citric Acid")
        residual_sugar = st.number_input("Residual Sugar")
        chlorides = st.number_input("Chlorides")
        free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide")
        total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide")

    with col2:
        density = st.number_input("Density")
        pH = st.number_input("pH")
        sulphates = st.number_input("Sulphates")
        alcohol = st.number_input("Alcohol")
        quality = st.number_input("Quality")

    with st.expander("Your Selected Options"):
        result = {
            'fixed acidity': fixed_acidity,
            'volatile acidity': volatile_acidity,
            'citric acid': citric_acid,
            'residual sugar': residual_sugar,
            'chlorides': chlorides,
            'free sulfur dioxide': free_sulfur_dioxide,
            'total sulfur dioxide': total_sulfur_dioxide,
            'density': density,
            'pH': pH,
            'sulphates': sulphates,
            'alcohol': alcohol,
            'quality': quality
        }

        st.write(result)

        encoded_result = []

        for i in result.values():
            encoded_result.append(i)

        st.write(encoded_result)

    with st.expander("Prediction Result"):
        single_sample = np.array(encoded_result).reshape(1, -1)
        st.write(single_sample)

        submenu = ["Logistic_Regression", "Decision Tree"]
        submenu = st.sidebar.selectbox("Submenu", submenu)

        # if submenu == "Logistic_Regression":
        #     st.subheader("Logistic Regression Model")

        #     model = load_model(r"http://localhost:8888/edit/df_pickle.pkl")
        #     prediction = model.predict(single_sample)
        #     st.write
if __name__ == "__main__":
    run_ml_app()