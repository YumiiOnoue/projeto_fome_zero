# ================================
# Importando Bibliotecas
# ================================
import plotly.express as px

# ================================
# Funções
# ================================
def top_rest(df):
    cols = [
    'restaurant_id', 'restaurant_name', 'country_code', 
    'city', 'cuisines', 'aggregate_rating', 'votes']
    df_aux = ( df.loc[:, cols]
                 .sort_values(['aggregate_rating', 'restaurant_id'], ascending=[False, True])
                 .head(10) )
    
    return df_aux

def maior_nota(df):
    df_aux = ( df.loc[:,['cuisines','aggregate_rating']]
                    .groupby('cuisines')
                    .max()
                    .sort_values('aggregate_rating', ascending=False)
                    .reset_index()
                    .head(10) )
    fig = px.bar(df_aux, x = 'cuisines', y = 'aggregate_rating', text_auto=True,
                        labels={'cuisines':'Tipo de Culinária','aggregate_rating':'Nota Média'})
    fig.update_layout(title_text='10 maiores notas médias por tipo de culinária')
    fig.update_traces(textposition='outside')
        
    return fig

def menor_nota(df):
    df_aux = ( df.loc[:,['cuisines','aggregate_rating']]
                    .groupby('cuisines')
                    .max()
                    .sort_values('aggregate_rating', ascending=True)
                    .reset_index()
                    .head(10) )
    fig = px.bar(df_aux, x = 'cuisines', y = 'aggregate_rating', text_auto=True,
                        labels={'cuisines':'Tipo de Culinária','aggregate_rating':'Nota Média'})
    fig.update_layout(title_text='10 menores notas médias por tipo de culinária')
    fig.update_traces(textposition='outside')
        
    return fig
        
