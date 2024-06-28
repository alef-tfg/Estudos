import streamlit as st 
import pandas as pd

st.title('Primeiro app streamlit')
st.subheader('Estudos aplicativos')
st.header('h1?')
st.text('paragrafo texto lorem')
st.markdown('---')
st.latex(r'\int_{a}^{b} x dx')
st.json({"a":"1,2,3", "b":"4,5,6"})
st.code("print('Hello world!')", language ='python')


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.write("Here's our first attempt at using data to create a table:")
st.write(df)

_df = st.data_editor(df)
number = list(_df['first column'])[0]

st.markdown(f'O número editado é {number}')
