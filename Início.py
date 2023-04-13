import pandas as pd
import numpy as np
import inflection
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
from utils import data

#====================================
# Carregando os Dados
#====================================

dataframe = pd.read_csv('dataset/zomato.csv')

df = dataframe.copy()

#=============================
# Limpando os dados
#=============================

# Renomeando colunas
df = data.rename_columns(df)

# Excluindo linhas sem dados
df = df.dropna()

# Categorizar restaurantes somente por um tipo de culinária
df['cuisines'] = df.loc[:, 'cuisines'].apply(lambda x: x.split(",")[0])

# Aplicando Tipo de Categoria de Comida
df["price_type"] = df.loc[:, "price_range"].apply(lambda x: data.create_price_tye(x))

# Aplicando o nome dos países
df["country_code"] = df.loc[:, "country_code"].apply(lambda x: data.country_name(x))

# Aplicando o nome das cores
df["color_name"] = df.loc[:, "rating_color"].apply(lambda x: data.color_name(x))

# Excluindo dados duplicados
df = df.drop_duplicates()

st.set_page_config(page_title='Início')

image = Image.open('logo.png')
st.sidebar.image(image, width=100)

st.sidebar.title( 'Fome Zero' )
st.sidebar.markdown( """---""" )

# ============= Layout no Streamlit ===============
st.title('Fome Zero')
st.markdown( """---""" )

st.markdown('A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.')

st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')

with st.container():
    col1, col2, col3, col4, col5 = st.columns( 5 )
    with col1:
        col1.metric(
            'Nº de Países',
            len(df['country_code'].unique()) )
        
    with col2:
        col2.metric(
            'Nº de Cidades',
            len(df['city'].unique()) )
        
    with col3:
        col3.metric(
            'Nº de Restauntes',
            len(df['restaurant_id'].unique()) )

    with col4:
        col4.metric(
            'Tipos de culinária',
            df['cuisines'].nunique() )
        
    with col5:
        col5.metric(
            'Total de avaliações feitas',
            df['votes'].sum() )
        
st.markdown('### Dashboard das principais métricas')
st.markdown(
    """
    Este dashboard foi organizado pelas seguintes visões:
    1. País
    2. Cidade
    3. Restaurante
        
    """
)
