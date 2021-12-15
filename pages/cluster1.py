import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium


def app():
    
    st.write("""
    ### Mapa vacío:
    """)
    mapavacio = folium.Map(location=[37.39161,-5.97640], zoom_start=12, tiles='CartoDB positron')
    folium_static(mapavacio)

    st.write("""
    ### Primera clusterización:
    """)
    f=codecs.open("Maps/primeros_clusters.html", 'r')
    mapa = f.read()
    components.html(mapa,height=550,scrolling=True)
    
    st.write("""
    ### Nos queda una zona de ruido:
    """)
    f2=codecs.open("Maps/zona_verde.html", 'r')
    mapa2 = f2.read()
    components.html(mapa2,height=550,scrolling=True)