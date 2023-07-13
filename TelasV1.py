import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np

#Nome no título da página
st.set_page_config(page_title="Dashboard")


#Criação do Menu
opcao = st.sidebar.selectbox(
    'Menu',
  ('Selecionar','Create QR Code','Contour Approximation','Open CV 1','Open CV 2')
)

#Criação das opções do Menu - Página principal
if opcao == 'Selecionar':
    st.title('Dashboard')
    st.markdown('## Alguma coisa na página principal ##')
    image_tab = Image.open('img/Tab1.jpg')
    st.image(image_tab)
    image_graf1 = Image.open('img/Graf1.jpg')
    st.image(image_graf1)
#
elif opcao == 'Create QR Code':
    st.title('Dashboard')
    st.markdown('## Create a new QR Code ##')
    title = st.text_input('Serial')
    title = st.text_input('Model')
    title = st.text_input('Date')

    #Faz o upload de uma imagem
    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
    st.button('Create')


elif opcao == 'Contour Approximation':
    st.title('QR Code Managemente')
    st.markdown('## Contour Approximation ##')
    image = st.selectbox('Select QR Code to process',
    ('10', '20', '30', '40')
    )
    if image == '10':   #Mostra imagem
        image_1 = Image.open('img/fig-1.jpg')
        st.image(image_1, caption='Imagem original')

        image_2 = Image.open('img/fig-2.jpg')
        st.image(image_1, caption='Imagem tratada')

  
elif opcao == 'Open CV 1':
    st.title('Visualisar imagens de visão computacional')

elif opcao == 'Open CV 2':
    st.title('Visualisar imagens de visão computacional')




