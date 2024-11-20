import  streamlit as st
import pandas as pd
import numpy as np
import time
import os
from dotenv import load_dotenv

synthesia_api_key = os.getenv("SYNTHESIA_API_KEY")


st.title("The Next School AI Avatar")
st.subheader("Hello! Welcome to the AI Avatar :wave:")
st.write('Ask anything')
with st.spinner('Wait for it...'):
    time.sleep(120)
    
st.write("Your AI is ready to talk to you!")





