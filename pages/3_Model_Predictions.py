import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.title('Using a Model to Predict')

@st.cache
def load_model(file):
    model_file = open(file, 'rb')
    loaded_model = joblib.load(model_file)
    model_file.close()
    return loaded_model

penguin_model = load_model('penguin_dt.pkl')

st.sidebar.title('Input using forms')
form1 = st.sidebar.form(key='Inputs')
form1.subheader('Bill Length and Depth')
bill_length = form1.number_input('Enter bill length (mm)', min_value = 0.0)
bill_depth = form1.number_input('Enter bill depth (mm)', min_value = 0.0)
form1.subheader('Flipper Length')
flipper_len = form1.number_input('Enter flipper lenth (mm)', min_value = 0.0)
body_mass = form1.number_input('Body mass (g)', min_value = 0.0)
sex = form1.number_input('Enter gender', help='Please enter 0 for male, or 1 for female', min_value = 0.0, max_value = 1.0)
island = form1.selectbox('Select the Island', options=['Torgersen', 'Biscoe', 'Dream'])
form_button = form1.form_submit_button('Submit features')

st.header('New Penguin Stats')
new_input = np.array([island, bill_length, bill_depth, flipper_len, body_mass, sex]).reshape(1,-1)
predict_in = pd.DataFrame(new_input, columns=penguin_model.feature_names_in_)
expander_df = st.expander('Show new penguin features')
expander_df.table(predict_in.loc[0])

predict_button = st.button('Predict the Species')
if predict_button:
    if float(predict_in['bill_length_mm'][0]) == 0.0:
        st.write('These are not valid stats for prediction')
    else:
        prediction = penguin_model.predict(new_input)
        st.write(f'According to our model the species of this penguin is {prediction[0]}')
