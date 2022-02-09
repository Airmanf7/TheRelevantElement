import streamlit as st
import pandas as pd
from helium import *
import shutil
import time
from selenium import webdriver
# from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from multiapp import MultiApp

from apps import home, headlines, wombo_tool, sec_wombo_tool #wombo_art_using_helium_driver # import your app modules here

relevant_element = MultiApp()

st.markdown("Some Text Here")

# Add all your applications here as tabs

relevant_element.add_app("Home", home.app)
relevant_element.add_app("Headlines", headlines.app)
relevant_element.add_app("Wombo Tool", sec_wombo_tool.generate)


# The main app
relevant_element.run()