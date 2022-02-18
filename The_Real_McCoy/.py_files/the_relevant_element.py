import streamlit as st
#import pandas as pd
#from helium import *
#from selenium import webdriver
#from newsapi import NewsApiClient
#from newsapi.newsapi_client import NewsApiClient
from multiapp import MultiApp

from apps import home, headlines, scan_for_articles, speech_recognition_and_search, wombo_tool, inspiring_quotes, donate_to_relevant_element

relevant_element = MultiApp()

st.markdown("The Relevant Element")


# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
relevant_element.add_app("Headlines", headlines.app)
relevant_element.add_app("Scan for Articles", scan_for_articles.app)
relevant_element.add_app("Speech to Search", speech_recognition_and_search.app)

relevant_element.add_app("Inspiring Quotes", inspiring_quotes.app)
relevant_element.add_app("Donate!", donate_to_relevant_element.app)

# The main app
relevant_element.run()