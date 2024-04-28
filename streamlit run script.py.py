#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st

# Load the trained logistic regression model
# You need to replace 'path_to_model.pkl' with the actual path to your trained model file
# Example: logistic_model = pickle.load(open('path_to_model.pkl', 'rb'))

# Define a function to make predictions
def predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked):
    # Convert Sex and Embarked to numerical format
    Sex = label_encoders['Sex'].transform([Sex])[0]
    Embarked = label_encoders['Embarked'].transform([Embarked])[0]
    
    # Make prediction using the trained model
    prediction = logistic_model.predict([[Pclass, Sex, Age, SibSp, Parch, Fare, Embarked]])
    
    return prediction[0]

# Streamlit app
st.title('Titanic Survival Prediction')

# User inputs
Pclass = st.selectbox('Passenger Class', [1, 2, 3])
Sex = st.selectbox('Sex', ['male', 'female'])
Age = st.slider('Age', 0, 100, 30)
SibSp = st.slider('Number of Siblings/Spouses Aboard', 0, 8, 0)
Parch = st.slider('Number of Parents/Children Aboard', 0, 6, 0)
Fare = st.number_input('Fare', min_value=0.0, max_value=1000.0, value=50.0)
Embarked = st.selectbox('Port of Embarkation', ['C', 'Q', 'S'])

# Predict survival
if st.button('Predict'):
    prediction = predict_survival(Pclass, Sex, Age, SibSp, Parch, Fare, Embarked)
    if prediction == 1:
        st.write('The passenger is predicted to survive.')
    else:
        st.write('The passenger is predicted not to survive.')

