# home.py

import streamlit as st
from streamlit_lottie import st_lottie 
import json



def home():
    st.set_page_config("College.ai",page_icon= '🏠', layout='centered')
    st.header("Welcome to the College.ai! 🏡")
    st.write("Explore the ChatGPT4 Features in free")

    
    with open('Home_student.json') as anim_source:
        animation = json.load(anim_source)
    st_lottie(animation, 1, True, True, "high", 350, -200)

    st.write("Project by: Suraj Sanap")



if __name__ == "__main__":
    home()
