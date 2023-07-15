import streamlit as st

import pickle

import numpy as np

with open('regression.pkl','rb') as file:

  regressor=pickle.load(file)

exp=st.number_input("Experience in Years:",0,42,1)

exp=np.array(exp).reshape(1,-1)

prediction=regressor.predict(exp)[0]

if st.button("Salary Prediction"):

    st.write(f"{prediction}")