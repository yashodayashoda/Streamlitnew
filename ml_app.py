# Framework Library
import streamlit as st
import joblib
import os



# Core Libraries
import pandas as pd
import numpy as np

attrib_info = """
Attribute Information:\n
Age 1.20-65;\n
Sex 1. Male, 2.Female;\n
Polyuria 1.Yes, 2.No.;\n
Polydipsia 1.Yes, 2.No.;\n
sudden weight loss 1.Yes, 2.No.;\n
weakness 1.Yes, 2.No.;\n
Polyphagia 1.Yes, 2.No.;\n
Genital thrush 1.Yes, 2.No.;\n
visual blurring 1.Yes, 2.No.;\n
Itching 1.Yes, 2.No.;\n
Irritability 1.Yes, 2.No.;\n
delayed healing 1.Yes, 2.No.;\n
partial paresis 1.Yes, 2.No.;\n
muscle stiffness 1.Yes, 2.No.;\n
Alopecia 1.Yes, 2.No.;\n
Obesity 1.Yes, 2.No.;\n
Class 1.Positive, 2.Negative.;
"""

label_dict = {"No":0,"Yes":1}
gender_map = {"Female":0,"Male":1}
target_label_map = {"Negative":0,"Positive":1}

# Fxns

def get_fvalue(val):
    feature_dict = {"No":0,"Yes":1}
    for key, value in feature_dict.items():
        if val == key:
            return value
        
def get_value(val):
    gender_map = {"Female":0,"Male":1}
    for key,value in gender_map.items():
	    if val == key:
		    return value 
        
def get_value(val,my_dict):
	for key,value in my_dict.items():
		if val == key:
			return value 

def load_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model



#  Main ML APP Function 

def run_ml_app():
    
    st.subheader("ML Prediction")
    
    with st.expander("Attributr Info"):
        st.write(attrib_info)
        
        
    # Layout
    
    col1,col2 = st.columns(2)
        
    with col1:
        age = st.number_input("Age",10,100)
        gender = st.radio("Gender",("Female","Male"))
        polyuria = st.radio("Polyuria",["No","Yes"])
        polydipsia = st.radio("Polydipsia",["No","Yes"]) 
        sudden_weight_loss = st.selectbox("Sudden_weight_loss",["No","Yes"])
        weakness = st.radio("weakness",["No","Yes"]) 
        polyphagia = st.radio("polyphagia",["No","Yes"]) 
        genital_thrush = st.selectbox("Genital_thrush",["No","Yes"]) 
            
    with col2:
        visual_blurring = st.selectbox("Visual_blurring",["No","Yes"])
        itching = st.radio("itching",["No","Yes"]) 
        irritability = st.radio("irritability",["No","Yes"]) 
        delayed_healing = st.radio("delayed_healing",["No","Yes"]) 
        partial_paresis = st.selectbox("Partial_paresis",["No","Yes"])
        muscle_stiffness = st.radio("muscle_stiffness",["No","Yes"]) 
        alopecia = st.radio("alopecia",["No","Yes"]) 
        obesity = st.select_slider("obesity",["No","Yes"]) 
              
    with st.expander("Your Selected Options"):
         result = {'age':age,
		'gender':gender,
		'polyuria':polyuria,
		'polydipsia':polydipsia,
		'sudden_weight_loss':sudden_weight_loss,
		'weakness':weakness,
		'polyphagia':polyphagia,
		'genital_thrush':genital_thrush,
		'visual_blurring':visual_blurring,
		'itching':itching,
		'irritability':irritability,
		'delayed_healing':delayed_healing,
		'partial_paresis':partial_paresis,
		'muscle_stiffness':muscle_stiffness,
		'alopecia':alopecia,
		'obesity':obesity}
        
         st.write(result)  
         
         encoded_result = []
         
         for i in result.values():
             if type(i) == int:
                 encoded_result.append(i)
             elif i in ['Male','Female']:
                res = get_value(i)
                encoded_result.append(res)
             else:
                 res1 = get_fvalue(i)
                 encoded_result.append(res1)
                 
         st.write(encoded_result)
         
    with st.expander("Prediction Result"):
        single_sample = np.array(encoded_result).reshape(1,-1)
        st.write(single_sample) 
    
        submenu = ["Logistic_Regression",'Decision Tree']
        submenu = st.sidebar.selectbox("Submenu",submenu)
        
        if submenu == "Logistic_Regression": 
            st.subheader("Logistic Regression Model")
            
            model = load_model(r"C:\Users\Windows\Downloads\Project_Streamlit-main\Project_Streamlit-main\data\diabetes_data_upload.csv http://localhost:8890/edit/df_pickle.pkl")
            prediction = model.predict(single_sample)
            st.write(prediction)
            
        else:
            st.subheader("Decision Tree")
            
            model = load_model(r"C:\Users\Windows\Downloads\Project_Streamlit-main\Project_Streamlit-main\data\diabetes_data_upload.csv http://localhost:8890/edit/df_pickle.pkl")
            prediction = model.predict(single_sample)
            st.write(prediction)
            
    
if __name__ == "__main__":
    run_ml_app()