import pandas as pd
import streamlit as st
from utilidades import leitura_de_dados
from utilidades import logo
from utilidades import contatos

logo()
contatos()

# Importando os dados para a página:

if 'dados' not in st.session_state:
    st.session_state['dados'] = None

leitura_de_dados()

df_vendas = st.session_state['dados']['df_vendas']
df_precos = st.session_state['dados']['df_precos']

# Configuração da Página
st.markdown('## 📁 Analítico')
st.divider()
tabela_selecionada = st.selectbox('Selecione a tabela desejada:',['Tabela de Vendas', 'Tabela de Preços'])

def mostrar_tabela_vendas():
    st.markdown("<br>", unsafe_allow_html=True)

    st.write(
    f'<div style="background-color:silver; color:black; padding:5px; border-radius:5px;text-align:center;">'
    f'<p style="font-size:16px;">\n Você selecionou a Tabela de Vendas! Para interagir, faça os filtros a seguir:</p>'
    f'</div>',
    unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    colunas_selecionadas = st.multiselect('Selecione as colunas inclusas nas tabela:',list(df_vendas.columns))
    col1,col2 = st.columns(2)
    filtro_selecionado = col1.selectbox('Selecione qual coluna você deseja filtrar:',list(df_vendas.columns))
    valores_unicos_colunas = (df_vendas[filtro_selecionado].unique())
    valor_filtro = col2.selectbox('Selecione o valor que você deseja filtrar:',valores_unicos_colunas)
    
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')
    
    if filtrar:
        st.dataframe(df_vendas.loc[df_vendas[filtro_selecionado] == valor_filtro,colunas_selecionadas])
    elif limpar:
        st.dataframe(df_vendas[colunas_selecionadas])
    else: 
        st.dataframe(df_vendas[colunas_selecionadas])

def mostrar_tabela_precos():
    st.markdown("<br>", unsafe_allow_html=True)
    st.write(
    f'<div style="background-color:silver; color:black; padding:5px; border-radius:5px;text-align:center;">'
    f'<p style="font-size:16px;">\n Você selecionou a Tabela de Preços! Para interagir, faça os filtros a seguir:</p>'
    f'</div>',
    unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    col1,col2 = st.columns(2)
    filtro_selecionado_2 = col1.selectbox('Selecione qual coluna você deseja filtrar:',list(df_precos.columns))
    valores_unicos_colunas_2 = (df_precos[filtro_selecionado_2].unique())
    valor_filtro_2 = col2.selectbox('Selecione o valor que você deseja filtrar:',valores_unicos_colunas_2)
    
    filtrar = col1.button('Filtrar')
    limpar = col2.button('Limpar')
    
    if filtrar:
        st.dataframe(df_precos.loc[df_precos[filtro_selecionado_2] == valor_filtro_2])
    elif limpar:
        st.dataframe(df_precos)
    else: 
        st.dataframe(df_precos)
    

if tabela_selecionada == 'Tabela de Vendas':
    mostrar_tabela_vendas()
    
if tabela_selecionada == 'Tabela de Preços':
    mostrar_tabela_precos()

# Carregando os dados para a página
