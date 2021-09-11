import streamlit as st
import pickle

Pkl_Filename = "Model.pkl"

with open(Pkl_Filename, 'rb') as file: 
    Regressor_model = pickle.load(file)
    

st.title('Salary Prediction Model')

yoe = st.sidebar.slider('Years of Expirience', 18, 60)

if st.sidebar.button('Predict'):
    output = Regressor_model.predict([[yoe]])
    st.write('The Predicted Salary is {}'.format(output))
    
    



