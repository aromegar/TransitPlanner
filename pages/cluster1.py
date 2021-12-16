import streamlit as st
from streamlit_folium import folium_static
import streamlit.components.v1 as components
import codecs
import folium
from PIL import Image


def app():
    
    st.write("""
    ### División de Sevilla en 606 secciones:
    """)
    
    f0=codecs.open("Maps/secc_densidad.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)

    st.write("""
    ### Población por secciones:
    """)
    
    f3=codecs.open("Maps/bubble_azul.html", 'r')
    mapa3 = f3.read()
    components.html(mapa3,height=550,scrolling=True)

    st.write("""
    ### Primera clusterización:
    """)
    
    rojo = Image.open("Maps/cluster0.png")
    st.image(rojo, use_column_width=True)
    
    st.write("""
    ### Proceso:
    """)
    
    proceso = Image.open("Images/eval63.png")
    st.image(proceso, use_column_width=True)
    
    proceso = Image.open("Images/modelo1.png")
    st.image(proceso, use_column_width=True)
    
    proceso = Image.open("Images/modelo2.png")
    st.image(proceso, use_column_width=True)
    
    proceso = Image.open("Images/modelo3.png")
    st.image(proceso, use_column_width=True)
    
    
    st.write("""
    ### Resultado:
    """)
    
    f1=codecs.open("Maps/primeros_clusters_size.html", 'r')
    mapa1 = f1.read()
    components.html(mapa1,height=550,scrolling=True)
    
    st.write("""
    ### Nos queda una zona de ruido:
    """)
    f2=codecs.open("Maps/zona_verde.html", 'r')
    mapa2 = f2.read()
    components.html(mapa2,height=550,scrolling=True)