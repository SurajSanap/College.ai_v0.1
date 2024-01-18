import streamlit as st
from streamlit_lottie import st_lottie 
import json

st.title("_           About               _")

st.header("Page:")
def Ask_To_PDF():
    st.markdown("1. Ask_To_PDF")
    with open('pdf.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)

    st.write("This service provides you the functionality to train the AI_Generative model \n on your PDF and then apply your query on it.")

def ATS():
    st.markdown("2. ATS")
    with open('ATS.json') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    st.write("Check if your resume is suitable for the job or not,\n Check if the job is good for you or not, \n Get recommendations based on your resume and job description.")

def ResumeAnalyzer():
    st.markdown("3. ResumeAnalyzer")
    with open('Resume.json', 'r', encoding='utf-8') as anim_source:
        animation = json.load(anim_source)
        st_lottie(animation, 1, True, True, "high", 100, -200)
    
    st.write("Check your resume's goodness \n Get recommendations for skills, fields, courses, etc.")

def show_thank_you_emoji():
    # Display 10 heart emojis
    hearts = " ❤️" * 3
    st.markdown(f"{hearts}")
    # Wait for 2 seconds
    time.sleep(2)

Ask_To_PDF()
ATS()
ResumeAnalyzer()
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

st.text("-                 This project is by Suraj Sanap                  -")
st.write("\n")

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.link_button('GitHub', "https://github.com/SurajSanap")
with col2:
    st.link_button('LinkedIn', "https://www.linkedin.com/in/surajsanap01")
with col3:
    if st.button('Thankyou'):
        try:
            show_thank_you_emoji()
        except:
            print("💝")
