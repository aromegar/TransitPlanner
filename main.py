from re import T
import streamlit as st
from PIL import Image
from multipage import MultiPage

from pages import home
from pages import oferta
from pages import cluster1
from pages import cluster2


app = MultiPage()


app.add_page("Index", home.app)
app.add_page("oferta actual", oferta.app)
app.add_page("1er cluster", cluster1.app)
app.add_page("2º cluster", cluster2.app)


app.run()