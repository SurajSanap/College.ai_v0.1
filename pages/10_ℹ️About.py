import streamlit as st
from streamlit_lottie import st_lottie 
import json


st.title("About")

st.header("               Page:                ")
def Ask_To_PDF():
    st.markdown("1. Ask_To_PDF")
    with open('pdf.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)

    st.write("This Service provide you the functionality to train the AI_Genrative model \n on your PDF and then Apply your query on it.")

def ATS():
    st.markdown("2. ATS")
    with open('ATS.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    st.write("Check your resume is suit for job or not,\n Check the Job is good for you or not, \n Get the recomendation besed on your Resume and Job Description.")

    
def ResumeAnalyzer():
    st.markdown("3. ResumeAnalyzer")
    with open('Resume.json', 'r', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    
    st.write("Check your resume's Goodness \n Get the recomendation skill, field, cources and etc")

Ask_To_PDF()
ATS()
ResumeAnalyzer()
st.text("-                           This is project by Suraj Sanap                  -")
st.write("\n")
st.link_button('GitHub',"https://github.com/SurajSanap")