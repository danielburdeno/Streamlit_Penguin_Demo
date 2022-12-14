import streamlit as st
import pandas as pd
import numpy as np
import joblib

from PIL import Image

st.sidebar.title('Change Name')
side_button = st.sidebar.button('Press Me!')
if side_button:
    st.sidebar.write('Sidebar button was pressed')


st.image('images/penguins.jpg', use_column_width='always')
st.title('Streamlit with Penguins')
st.header('This is a header')

col1, col2 = st.columns(2)
col1.subheader('Col1')
col2.subheader('Col2')

col21, col22, col23 = st.columns([3,2,1])
col21.write('Widest column, testing 1 2 3, text should wrap if it need too')
col22.write('Medium col, mic check')
col23.write('Small col, succes')

st.markdown('Markdown **syntax** *works*')
'Markdown'
'# Magic'

st.write('<h2 style="text-align:center">Text aligned with HTML</h2', unsafe_allow_html=True)

check = st.checkbox('Please check me!')

button_check = st.button('Is box checked?')
if button_check:
    if check:
        st.write('The box was checked')
    else:
        st.write('Not checked')

animal_options = ['Cats', 'Dogs', 'Guinea Pig', 'Bearded Dragons']

fav_animal = st.radio('Which animal is your favorite', animal_options)
button_fav = st.button('Submit Animal')
if button_fav:
    st.write(f'You selected {fav_animal} as your fav animal')
    if fav_animal == 'Cats':
        st.write('MEOW')
    if fav_animal == 'Dogs':
        st.write('WHOOF')
    else:
        st.write('animal noise')

fav_animal2 = st.selectbox('Fav Animal?', animal_options)
button_fav2 = st.button('Submit')
if button_fav2:
    st.write(f'You selected {fav_animal} as your fav animal')
    if fav_animal == 'Cats':
        st.write('MEOW')
    if fav_animal == 'Dogs':
        st.write('WHOOF')
    else:
        st.write('animal noise')

animals_like = st.multiselect('Which animals do you like?', animal_options)
button_like = st.button('Animals')
if button_like:
    st.write(animals_like)
    st.write(f'Your first submission was {animals_like[0]}')

num_pets = st.slider('How many pets do you have?')

in_text = st.text_input('What is your pets name?', value="I don't have a pet")
st.write("Pet's name is:", in_text)

num_input = st.number_input("How many pets?", min_value=0)
st.write(f'I have {num_input} pets')