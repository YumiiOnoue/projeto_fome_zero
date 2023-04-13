# ================================
# Importando Bibliotecas
# ================================
import plotly.express as px

# ================================
# Funções
# ================================
def rest_by_city(df):
    df_aux = ( df.loc[:, ['restaurant_id', 'city']]
                            .groupby('city')
                            .count()
                            .sort_values('restaurant_id', ascending=False)
                            .reset_index()
                            .head(10) )
    fig = px.bar(df_aux, x = 'city', y = 'restaurant_id', text_auto=True,
                    labels={'city':'Cidade','restaurant_id':'Qtd. Restaurantes Registrados'})
    fig.update_layout(title_text='Número de restaurantes registrados por cidade')
    fig.update_traces(textposition='outside')
    
    return fig

def bem_avaliado(df):
    boa_avaliacao = ( df.loc[df['aggregate_rating']>=4 ,['city', 'restaurant_id']]
                    .groupby('city')
                    .count()
                    .sort_values('restaurant_id', ascending=False)
                    .reset_index()
                    .head(10) )
    fig = px.bar(boa_avaliacao, x = 'city', y = 'restaurant_id', text_auto=True,
                        labels={'city':'Cidade','restaurant_id':'Qtd. Restaurantes'})
    fig.update_layout(title_text='Cidade com mais restaurantes bem avaliados')
    fig.update_traces(textposition='outside')
    
    return fig
    
def mal_avaliacao(df):
    ruim_avaliacao = ( df.loc[df['aggregate_rating'] <= 2.5,['city','restaurant_id']]
                           .groupby('city')
                           .count()
                           .sort_values('restaurant_id', ascending=False)
                           .reset_index()
                           .head(10) )
    fig = px.bar(ruim_avaliacao, x = 'city', y = 'restaurant_id', text_auto=True,
                        labels={'city':'Cidade','restaurant_id':'Qtd. Restaurantes'})
    fig.update_layout(title_text='Cidade com mais restaurantes mal avaliados')
    fig.update_traces(textposition='outside')
        
    return fig

def qtd_culinaria(df):
    culinaria_distinta = ( df.loc[:, ['city', 'cuisines']]
                            .groupby('city')
                            .nunique()
                            .sort_values('cuisines', ascending=False)
                            .reset_index()
                            .head(10) )
    fig = px.bar(culinaria_distinta, x = 'city', y = 'cuisines', text_auto=True,
                        labels={'city':'Cidade','cuisines':'Tipos de Culinária'})
    fig.update_layout(title_text='Cidade com maior quantidade de culinárias distintas')
    fig.update_traces(textposition='outside')
    
    return fig

def reserva(df):
    reservas = ( df.loc[df['has_table_booking']==1, ['city', 'restaurant_id']]
                    .groupby('city')
                    .count()
                    .sort_values('restaurant_id', ascending=False)
                    .reset_index()
                    .head(10) )
    fig = px.bar(reservas, x = 'city', y = 'restaurant_id', text_auto=True,
                        labels={'city':'Cidade','restaurant_id':'Qtd. Restaurantes'})
    fig.update_layout(title_text='Top cidade que fazem reservas')
    fig.update_traces(textposition='outside')
        
    return fig

def entrega(df):
    lines = (df['has_online_delivery'] == 1) & (df['is_delivering_now'] == 1)
    entregas = ( df.loc[lines, ['city', 'restaurant_id']]
                    .groupby('city')
                    .count()
                    .sort_values('restaurant_id', ascending=False)
                    .reset_index()
                    .head(10) )
    fig = px.bar(entregas, x = 'city', y = 'restaurant_id', text_auto=True,
                        labels={'city':'Cidade','restaurant_id':'Qtd. Restaurantes'})
    fig.update_layout(title_text='Top cidade que aceitam pedidos online e entregam')
    fig.update_traces(textposition='outside')
        
    return fig
    
        
