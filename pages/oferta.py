import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium


def app():
    
    st.write("""
    ### Oferta actual de bicis / buses:
    """)
    f0=codecs.open("Maps/bici-bus-grupos.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)