from models import loader
import streamlit as st
import numpy as np


def titanic_survival_classifier(data):
    """ This is a function that is used to predict chances of survival for a passenger using input dataset provided by the user. """

    # Data encoding
    # 1. ticket class
    if data["Pclass"] == 'First class (upper class)':
        ticket_class = 1
    elif data["Pclass"] == 'Second class (middle class)':
        ticket_class = 2
    else:
        ticket_class = 3
    
    # 2. Gender
    if data["Gender"] == 'Female':
        gender = 0
    
    else:
        gender = 1
    
    # 3. Embarking port
    if data["Embarked"] == 'Southampton':
        embarking_port = 0

    elif data["Embarked"] == 'Cherbourg':
        embarking_port = 1
    
    else:
        embarking_port = 2

    cleaned_data = (ticket_class, gender, data["Age"], data["SibSp"], data["ParCh"], data["Fare"], embarking_port)
    cleaned_data = np.asarray(cleaned_data).reshape(1, -1)
    prediction = loader.titanic_survival_model.predict(cleaned_data)

    if prediction[0] == 0:
        return st.error(f'Prediction: Passenger "{data["Name"]}" may not survive!', icon='☠️')
    
    else:
        return st.success(f'Prediction: Passenger "{data["Name"]}" will survive', icon='🫡')
