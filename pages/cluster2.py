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
    
    st.write("""
    ### repetimos el proceso:
    """)
    
    rojo = Image.open("Maps/cluster00.png")
    st.image(rojo, use_column_width=True)
    
    proceso = Image.open("Images/modelo4.png")
    st.image(proceso, use_column_width=True)
        
    st.write("""
    ### y obtenemos los 34 clusters finales...
    """)
    f0=codecs.open("Maps/bubble_34.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)
    
    st.write("""
    ### ...con sus centroides ponderados :
    """)
    f0=codecs.open("Maps/bubble_34_centroides.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)
    
    st.write("""
    ### Agrupamos población en una única burbuja por parada... :
    """)
    f0=codecs.open("Maps/bubble_paradas.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)
    
    st.write("""
    ### ...y contrastamos con paradas existentes :
    """)
    f0=codecs.open("Maps/bubble_paradas+act.html", 'r')
    mapa0 = f0.read()
    components.html(mapa0,height=550,scrolling=True)