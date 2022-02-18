from PIL import Image
import glob
import streamlit as st

def app():
    st.title('Art Gallery')

    st.write('Enjoy this art gallery!')



    col1, col2, col3, col4 = st.columns(4)
    image_list = []
    for filename in glob.glob('C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//The_Real_McCoy//resources//Images//WomboArtWorks//*.jpg'): # Gets only jpg files
        im=Image.open(filename)
        image_list.append(im)

    with col1:

        st.image(image_list[0:5], width=200)

    with col2:
        st.image(image_list[6:10], width=200)

    with col3:
        st.image(image_list[11:15], width=200)

    with col4:
        st.image(image_list[16:20], width=200)  

