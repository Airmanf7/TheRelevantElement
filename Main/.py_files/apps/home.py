from random import randint
import streamlit as st
import time
import os
import pandas as pd
import time
import streamlit as st
from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from PIL import Image
import base64


def app():

    st.title('Welcome to The Relevant Element')

    ### gif from local file
    file_ = open("C://Users//Airma//FinTechClass//Project_3_TheRelevantElement//Main//resources//Images//element.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
    )

    def top_headlines():
        news_api_key = os.getenv("news_api_key")
        newsapi = NewsApiClient(api_key="6979450998b44ae483661232ae2c1fd3")
        top_articles = newsapi.get_top_headlines(country="us", language='en')

        return top_articles

    top_headlines_df = pd.DataFrame.from_dict(top_headlines()['articles'])
    top_headlines_df["source"] = top_headlines_df["source"].apply(lambda x: x['name'])


    
    images = ["https://ipfs.io/ipfs/QmeTuPqzFWosFkCycvoN29jkfbMXDGWMMLMBMnStYXMW5W?filename=Dream.jpg",
              "https://ipfs.io/ipfs/QmNZAoco2BLbTnpqyBMmJ2CkH3ncoMbJofKWfRC9jX9UCy?filename=everything_is_awesome.jpg",
              "https://ipfs.io/ipfs/QmR1UCsrPNAUPKPtB133VtUMkyhTFLaqepmLnqkfahrHWU?filename=Family_and_Love.jpg",
              "https://ipfs.io/ipfs/QmV5nZAeLJmmWknrfQEPxNba8JUqA5dpd8ZWdJtSanXkVz?filename=The_hot_sauce_is_mine.jpg"
              "https://ipfs.io/ipfs/QmVvdRRgUXDHuRR5Bd9FiYXFptsThqdouJdDxXGB2pA4Uc?filename=thief_in_the_night.jpg"
              ]

    captions = ["Dream", "Everything is Awesome", "Family and Love", "The hot sauce is mine", "Thief in the night"]




##############################################################################################################
# Streamlit Integration #
##############################################################################################################

    if st.button('Start!'):
            st.write("Launching The Relevant Element...")
            time.sleep(3)
            st.spinner("")

            my_bar = st.progress(0)

            for percent_complete in range(100):
                time.sleep(0.05)
                my_bar.progress(percent_complete + 1)

            st.write('Here are some Headlines!')

            index = 0   
            for row in top_headlines_df['title']:
                st.write(top_headlines_df['title'][index])
                time.sleep(1)
                index += 1
                if index == 5: # Break the loops after 5 articles are displayed
                    break
        
                



   

    



    

    