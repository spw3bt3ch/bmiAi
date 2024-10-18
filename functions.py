import streamlit as st
from main import *
import requests


def ai(bmi_result, username):
    url = "https://chatgpt-42.p.rapidapi.com/conversationgpt4-2"
    
    payload = {
    	"messages": [
    		{
    			"role": "user",
    			"content": "hello"
    		}
    	],
    	"system_prompt": "",
    	"temperature": 0.9,
    	"top_k": 5,
    	"top_p": 0.9,
    	"max_tokens": 256,
    	"web_access": False
    }
    headers = {
    	"x-rapidapi-key": "4d7f06c497msh8ae3ad75c4ed8a9p1c158fjsn39f68bdb2dc7",
    	"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
    	"Content-Type": "application/json"
    }
    
    response = requests.post(url, json=payload, headers=headers)

    resp = dict(response.json())
    for k, v in resp.items():
        st.info(f"{k.upper()}: {v}")
