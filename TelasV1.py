import streamlit as st
import pandas as pd

#Nome no título da página
st.set_page_config(page_title="Dashboard")

import streamlit as st

st.title('Dashboard')


#st.button('Listar e deletar')




opcao = st.sidebar.selectbox(
    'Menu',
  ('Selecionar','Listar e deletar','Criar','Entrar','Open CV 1','Open CV 2')
)

if opcao == 'Listar e deletar':
    st.write('Você quer listar e deletar')

elif opcao == 'Criar':
    st.write('Você quer criar')

elif opcao == 'Entrar':
    st.write('Você quer entar')

elif opcao == 'Open CV 1':
    st.write('Visualisar imagens de visão computacional')

elif opcao == 'Open CV 2':
    st.write('Visualisar imagens de visão computacional')




