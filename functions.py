import streamlit as st
from main import *
import requests


def ai(bmi_result, username):
    url = "https://open-ai21.p.rapidapi.com/claude3"
    
    payload = {
    	"messages": [
    		{
    			"role": "user",
    			"content": f"An extremely short medical advice for {username} with a bmi value of {bmi_result}, address the name in your response"
    		}
    	],
    	"web_access": False
    }
    headers = {
    	"x-rapidapi-key": "4d7f06c497msh8ae3ad75c4ed8a9p1c158fjsn39f68bdb2dc7",
    	"x-rapidapi-host": "open-ai21.p.rapidapi.com",
    	"Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)

    resp = dict(response.json())
    for k, v in resp.items():
        st.info(f"{k.upper()}: {v}")
