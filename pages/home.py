import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import codecs

def app():
    portada = Image.open("images/930009.jpg")
    st.image(portada, use_column_width=True)
    
    st.write("""
    # Transit Planner
    ## Al cobete 🚀
    Este es mi proyecto y bla bla
    """)