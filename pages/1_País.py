# ================================
# Importando Bibliotecas
# ================================

import pandas as pd
import numpy as np
import inflection
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import folium
from streamlit_folium import folium_static
from utils import data, pais_data

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

# ======================================
# Streamlit
# ======================================

st.title('Visão: País')
st.markdown( """---""" )

# ======= Sidebar ====================

image = Image.open('logo.png')
st.sidebar.image(image, width=100)

st.sidebar.title( 'Fome Zero' )
st.sidebar.markdown( """---""" )

# Filtros do sidebar
countries = st.sidebar.multiselect(
        "Escolha os países que deseja visualizar os restaurantes",
        df.loc[:, "country_code"].unique().tolist(),
        default=["Brazil", "England", "Qatar", "South Africa", "Canada", "Australia"],
    )
linhas_selecionadas = df['country_code'].isin(countries)
df = df.loc[linhas_selecionadas, :]

# ============= Layout no Streamlit ===============

tab1, tab2, tab3 = st.tabs(['Visão Geral', 'Avaliações', '-'])

with tab1:
    with st.container():
        fig = pais_data.qtd_cidade(df)
        st.plotly_chart(fig, use_container_width=True)

    with st.container():
        fig = pais_data.qtd_restaurante(df)
        st.plotly_chart(fig, use_container_width=True)
                  
    with st.container():
        fig = pais_data.rest_gourmet(df)
        st.plotly_chart(fig, use_container_width=True)
                 
    with st.container():  
        fig = pais_data.culinaria(df)
        st.plotly_chart(fig, use_container_width=True)             
                     
    with st.container():
        fig = pais_data.entrega(df)
        st.plotly_chart(fig, use_container_width=True)
                     
    with st.container():
        fig = pais_data.reserva(df)
        st.plotly_chart(fig, use_container_width=True)       

with tab2:                                          
    with st.container():
        col1, col2 = st.columns( 2, gap='large' )
        with col1:
            st.markdown('Quantidade de avaliações feitas')
            df_aux = pais_data.avaliacao(df)
            st.dataframe(df_aux)
            
        with col2:
            with st.container():
                df_aux = pais_data.nota_media(df, top_asc=True)
                col2.metric( 'País com menor nota média registrada', df_aux )
                     
                df_aux = pais_data.nota_media(df, top_asc=False)  
                col2.metric( 'País com maior nota média registrada', df_aux )
