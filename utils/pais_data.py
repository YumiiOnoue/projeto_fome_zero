# ================================
# Importando Bibliotecas
# ================================
import plotly.express as px

# ================================
# Funções
# ================================
def qtd_cidade(df):
    df_aux =( df.loc[:, ['country_code', 'city']]
                    .groupby('country_code')
                    .nunique()
                    .sort_values('city', ascending=False)
                    .reset_index() )
    fig = px.bar(df_aux, x = 'country_code', y = 'city', text_auto=True,
                    labels={'country_code':'País','city':'Qtd. Cidade'})
    fig.update_layout(title_text='Quantidade de cidades registradas')
    fig.update_traces(textposition='outside')
    
    return fig

def qtd_restaurante(df):
    df_aux = ( df.loc[:, ['country_code', 'restaurant_id']]
                     .groupby('country_code')
                     .nunique()
                     .sort_values('restaurant_id', ascending=False) 
                     .reset_index() )
    fig = px.bar(df_aux, x = 'country_code', y = 'restaurant_id', text_auto=True,
                    labels={'country_code':'País','restaurant_id':'Qtd. Restaurantes'})
    fig.update_layout(title_text='Quantidade de restaurantes registrados')
    fig.update_traces(textposition='outside')
    
    return fig

def rest_gourmet(df):
    df_aux = ( df.loc[df['price_range']==4, ['country_code', 'restaurant_id', 'price_range']]
                     .groupby('country_code')
                     .count()
                     .sort_values('restaurant_id', ascending=False)
                     .reset_index() )
    fig = px.bar(df_aux, x = 'country_code', y = 'price_range', text_auto=True,
                    labels={'country_code':'País','price_range':'Qtd. Restaurantes Gourmet'})
    fig.update_layout(title_text='Número de restaurantes gourmet')
    fig.update_traces(textposition='outside')
    
    return fig

def culinaria(df):
    df_aux = ( df.loc[:, ['country_code', 'cuisines']]
                     .groupby('country_code')
                     .nunique()
                     .sort_values('cuisines', ascending=False)
                     .reset_index() )
    fig = px.bar(df_aux, x = 'country_code', y = 'cuisines', text_auto=True,
                    labels={'country_code':'País','cuisines':'Qtd. Culinária'})
    fig.update_layout(title_text='Quantidade de tipos de culinária distintas')
    fig.update_traces(textposition='outside')

    return fig

def entrega(df):
    df_aux = ( df.loc[df['is_delivering_now']==1, ['country_code', 'is_delivering_now']]
                     .groupby('country_code')
                     .count()
                     .sort_values('is_delivering_now', ascending=False)
                     .reset_index() )
    fig = px.bar(df_aux, x = 'country_code', y = 'is_delivering_now', text_auto=True,
                    labels={'country_code':'País','is_delivering_now':'Qtd. Delivery'})
    fig.update_layout(title_text='Quantidade de restaurantes que fazem entrega')
    fig.update_traces(textposition='outside')
        
    return fig

def reserva(df):
    df_aux = ( df.loc[df['has_table_booking']==1, ['country_code', 'has_table_booking']]
                     .groupby('country_code')
                     .count()
                     .sort_values('has_table_booking', ascending=False)
                     .reset_index())
    fig = px.bar(df_aux, x = 'country_code', y = 'has_table_booking', text_auto=True,
                    labels={'country_code':'País','has_table_booking':'Qtd. Reserva'})
    fig.update_layout(title_text='Quantidade de restaurantes que aceitam reservas')
    fig.update_traces(textposition='outside')
        
    return fig
    
def avaliacao(df):
    df_aux = ( df.loc[:, ['country_code', 'votes']]
                 .groupby('country_code')
                 .sum()
                 .sort_values('votes', ascending=False)
                 .reset_index() )
    return df_aux

def nota_media(df, top_asc):
    df_aux = ( df.loc[:, ['country_code','aggregate_rating']]
                     .groupby('country_code')
                     .mean()
                     .sort_values('aggregate_rating', ascending=top_asc)
                     .reset_index()
                     .iloc[0,0] )
    return df_aux