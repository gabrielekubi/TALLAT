import streamlit as st                
import time
import os
import numpy as np
import pandas as pd
from datetime import datetime
import re
from PIL import Image

st.set_page_config(
    layout='wide',
    page_icon=Image.open("logo.ico"),
    page_title='TALLAT')            
#add_logo("http://placekitten.com/120/120")





#file_buffer = st.sidebar.file_uploader("Upload a xlsx file")

tab1 = st.tabs(["Diseña tu propio llavero"])

# Lista de tipos de llaveros
tipos_llaveros = ["Cuadrado", "Rectangular", "Redondo", "Ovalado"]




col1, col2, col3 = st.columns([1,1,1])

# Selector de tipo de llavero
with col1:
    tipo_seleccionado = st.selectbox("Selecciona el tipo de llavero", tipos_llaveros)
    #dibujo_seleccionado = st.selectbox("Selecciona el dibujo", ['Corona de flores'])
    file_buffer = st.file_uploader("Upload a .png file")

#with col2:
#    st.image('imagenes_llaveros\\' + str(tipo_seleccionado) + '.jpg' , width=300)        

if file_buffer is not None:

    imagen_llavero = Image.open('imagenes_llaveros/' + str(tipo_seleccionado) + '.jpg' )
    imagen_dibujo = Image.open(file_buffer)

    with col1:
        tamano = st.select_slider('Selecciona tamaño del dibujo', range(1,301), 50)

    # Redimensiona el dibujo para que se ajuste al llavero
    imagen_dibujo = imagen_dibujo.resize((tamano, tamano))  # Cambia el tamaño según sea necesario

    with col3:
        pos_x = st.select_slider('Selecciona posición X del dibujo', range(0,801), 50)
        pos_y = st.select_slider('Selecciona posición Y del dibujo', range(0,801), 50)
        angulo = st.select_slider('Selecciona el giro del dibujo', range(0,361), 0)
        st.text(angulo)


    # Abrir y girar la imagen del dibujo
    imagen_dibujo_rotada = imagen_dibujo.rotate(angulo, expand=True)

    # Superponer el dibujo rotado sobre el llavero
    imagen_llavero.paste(imagen_dibujo_rotada, (pos_x, pos_y), imagen_dibujo_rotada)


    # Superpone el dibujo sobre el llavero
    #imagen_llavero.paste(imagen_dibujo, (pos_x, pos_y), imagen_dibujo)  # Cambia las coordenadas (50, 50) según sea necesario

    with col2:
    # Muestra la imagen resultante
        st.image(imagen_llavero, width=500)
