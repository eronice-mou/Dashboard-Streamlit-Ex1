import streamlit as st
import pandas as pd
from pandas import read_csv

st.set_page_config(page_title="Meu site Streamlit")

with st.container():
    st.title("Dashboard Covid 19")



tabela = pd.read_csv("vaccination-data.csv")
st.write(tabela)

if st.button('GERAR GRÁFICO DE BARRAS'):
    st.write("---")
    st.bar_chart(tabela, x="DATE_UPDATED", y="TOTAL_VACCINATIONS")

if st.button('GERAR GRÁFICO DE LINHA'):
    st.write("---")
    st.line_chart(tabela, x="DATE_UPDATED", y="TOTAL_VACCINATIONS")
 