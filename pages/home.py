import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

def app():
    
    st.write("""
    # Transit Planner :tram:
    (C) Alfonso Romero -Ironhack DAFT-OCT21
    """)
    
    portada = Image.open("images/930009.jpg")
    st.image(portada, use_column_width=True)
    
    st.write("""
    ## Proposing new stations for Metro de Sevilla""")