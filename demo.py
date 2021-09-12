import streamlit as st
import pickle


# "/app/{repository name}/ {file.extension}"
Pkl_Filename = "/app/pickle_demo_streamlit/Model.pkl"

with open(Pkl_Filename, 'rb') as file: 
    Regressor_model = pickle.load(file)
    

st.title('Salary Prediction Model')

yoe = st.sidebar.slider('Years of Expirience', 18, 60)

if st.sidebar.button('Predict'):
    output = Regressor_model.predict([[yoe]])
    st.write('The Predicted Salary is {}'.format(output))
    
    



