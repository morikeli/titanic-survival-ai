from models import loader
import streamlit as st
import numpy as np


def titanic_survival_classifier(data):
    data = np.asarray(data).reshape(1, -1)
    prediction = loader.titanic_survival_model.predict(data)

    if prediction[0] == 0:
        return st.success('Prediction: Non-diabetic', icon='🫡')
    
    else:
        return st.error('Prediction: You may not survive!', icon='☠️')