import streamlit as st
from streamlit_lottie import st_lottie 
import json
st.title("Resume_Analyser with AI")

with open('commingsoon.json', 'r', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 400, -200)