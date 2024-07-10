import pandas as pd
import streamlit as st
from utilidades import leitura_de_dados
from utilidades import logo
from utilidades import contatos
from datetime import datetime
from datetime import date
import plotly.express as px

logo()
contatos()

df_precos = pd.read_csv('dataset/padaria_preco.csv', decimal='.', sep=',', index_col=0, parse_dates=True)
df_vendas = pd.read_csv('dataset/padaria_venda.csv', decimal='.', sep=',', index_col='id_vendas', parse_dates=['data'])

# Se df_vendas for None ou vazio, inicializa com um DataFrame vazio
if df_vendas is None:
    df_vendas = pd.DataFrame(columns=['id_vendas', 'data', 'produto', 'quantidade', 'modo_pagamento'])

# Interface do Streamlit
st.markdown('## 📊 Dashboard')
st.divider()

df_vendas = pd.merge(left=df_vendas,
                     right=df_precos,
                     on='produto',
                     how='left')


# FORMATANDO DATAS

df_vendas['data'] = pd.to_datetime(df_vendas['data'], format='%d-%m-%Y %H:%M:%S', errors='coerce')

# Filtrar linhas com datas válidas
df_vendas = df_vendas.dropna(subset=['data'])

# Obter a maior e a menor data válida
data_final_def = df_vendas['data'].max()

# Criar data inicial no formato datetime64[ns]
data_inicial_def = pd.to_datetime(data_final_def.replace(day=1))

# Inputs de data inicial e final no Streamlit
col1, col2 = st.columns(2)
data_inicial = col1.date_input('Data Inicial', data_inicial_def.date() if not pd.isnull(data_inicial_def) else datetime.today().date())
data_final = col2.date_input('Data Final', data_final_def.date() if not pd.isnull(data_final_def) else datetime.today().date())

# Converter data_inicial e data_final para datetime64[ns]
data_inicial = pd.to_datetime(data_inicial)
data_final = pd.to_datetime(data_final)

# Filtrar o DataFrame com base nas datas selecionadas
df_vendas_corte = df_vendas[(df_vendas['data'] >= data_inicial) & (df_vendas['data'] <= data_final)]

# Exibir o DataFrame filtrado
#st.dataframe(df_vendas_corte)

# FORMATANDO AS METRICAS

# Metrica 1: kpi

valor_vendas = f"R${df_vendas_corte['preco_unitario'].sum()}"
col1.metric("Receita de Vendas",valor_vendas)

produtos_vendidos = len(df_vendas_corte)
col2.metric("Qntd. de Vendas",produtos_vendidos)

df_mes = df_vendas.groupby(df_vendas['data'].dt.strftime('%Y-%m'))['preco_unitario'].sum().reset_index()
grafico_mes = px.bar(df_mes, x='preco_unitario', y='data', orientation='h',labels={'data': 'Mês', 'preco_unitario': 'Receita'},text_auto='.2s',title="Receita por Mês",color_discrete_sequence=px.colors.sequential.RdPu)
col1.plotly_chart(grafico_mes)

df_pizza = df_vendas_corte.groupby('produto')['preco_unitario'].sum().reset_index()
grafico_pizza = px.pie(df_vendas_corte, values='preco_unitario', names='produto',title="Percentual de Produtos Vendidos",color_discrete_sequence=px.colors.sequential.RdPu)
col2.plotly_chart(grafico_pizza)

# GRAFICO DE RECEITA POR PRODUTO
fig = px.histogram(df_vendas_corte, x='produto', y='preco_unitario', title="Receita por produto",text_auto='.2s',color='preco_unitario',color_discrete_sequence=px.colors.sequential.RdPu,labels={'produto': 'Produto', 'preco_unitario': 'Receita'})
st.plotly_chart(fig)

