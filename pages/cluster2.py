import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
from PIL import Image


def app():
    
    st.write("""
    ### Volvemos a clusterizar el ruido:
    """)
    
    f0=codecs.open("Maps/zona_verde.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)