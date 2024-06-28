import langchain_helper_pet as lch
import streamlit as st

st.title("Pets name generator")
animal_type = st.sidebar.selectbox("What is your pat?", ("Cat", "Dog", "Cow", "Snake", "Lizard"), index = None)

if animal_type != None:
    pet_color = st.sidebar.text_area(f"What color is your {animal_type.lower()}?",
                                     max_chars=15)


def generate_response():
    if (animal_type != None) and (pet_color != ''):
        response = lch.generate_pet_name(animal_type, pet_color)
        st.write(response['pet_name'])



response = st.sidebar.button("Generate", type="primary", on_click=generate_response)

