# Initial Imports

import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from helium import *
import time
from fpdf import FPDF
import base64

def app():

    st.title('Speech Recognition')


    st.write('Speech recognition software is used to capture speech and search for top results')

    show_elements = []

    # Initialize the speech recognition engine

# Set the microphone to listen to the user and convert the audio to text; no set time limit

    if st.button('Start Listening and Search'):
        def get_audio():
            r = sr.Recognizer()
            with sr.Microphone() as source:

                audio = r.listen(source)
                said = ""

            try:
                said = r.recognize_google(audio)
            
            except Exception as e:
                print("Exception:" + str(e))

            return said
    
        element = get_audio() # get the audio from the user and convert to text
    
        # append the text to the list, run a google search with the text, and display a .gif while the search is running
        show_elements.append(element)
        st.write("The Current Element")
        st.write('Searching for ' + element)
        # Add a button to start over
        if st.button("Start Over"):
            helium.kill_browser() 

        ### gif from local file
        file_ = open("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//Main//resources//Images//matrix.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
        unsafe_allow_html=True,
        )
        # if st.button("Start Over"):
        #     helium.kill_browser() 

        time.sleep(5)
        helium.start_chrome('https://www.google.com/search?q=' + element)

        


