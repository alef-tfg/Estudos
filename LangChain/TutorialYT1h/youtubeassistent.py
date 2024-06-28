import streamlit as st
import langchain_helper_youtube as lch
import textwrap

st.title("Assistente do youtube")

with st.sidebar:
    with st.form(key='my_form'):
        youtube_url = st.sidebar.text_area(
            label="Cole aqui a url do video do youtube",
            max_chars=50
        )
        query = st.sidebar.text_area(
            label="O que você que saber sobre o video?",
            max_chars=50,
            key="query"
        )

        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url:
    db = lch.create_vector_db_from_youtube_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Resposta:")
    st.text(textwrap.fill(response, width= 80))
         
