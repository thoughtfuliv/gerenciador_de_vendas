# Importando as bibliotecas necessárias
import pandas as pd
import streamlit as st
from datetime import datetime
from utilidades import logo
from utilidades import contatos

# Importando os elementos da sidebar
logo()
contatos()

# Carregar os DataFrames diretamente dos arquivos CSV
df_precos = pd.read_csv('dataset/padaria_preco.csv', decimal='.', sep=',', index_col=0, parse_dates=True)
df_vendas = pd.read_csv('dataset/padaria_venda.csv', decimal='.', sep=',', index_col='id_vendas', parse_dates=['data'])

# Se df_vendas estiver vazio, inicializa com um DataFrame vazio
if df_vendas.empty:
    df_vendas = pd.DataFrame(columns=['data', 'produto', 'quantidade', 'modo_pagamento'])

# Função para atualizar o id_vendas
def atualizar_id_vendas():
    df_vendas.reset_index(drop=True, inplace=True)
    df_vendas['id_vendas'] = range(1, len(df_vendas) + 1)
    df_vendas.set_index('id_vendas', inplace=True)

# Interface do Streamlit
st.markdown('## 📈 Gestão das Vendas')
st.divider()

# Módulo 1: Adição de Vendas
st.markdown('### Adição de Vendas')

produto_adicionado = df_precos['produto'].tolist()
valor_produto_filtro = st.selectbox("Selecione o produto vendido:", produto_adicionado)

quantidade_adicionado = st.selectbox("Selecione a quantidade vendida:", [1, 2, 3, 4, 5])

valor_modo_filtro = st.selectbox("Selecione o modo de pagamento:", ["pix", "debito", "credito"])

adicionar_venda = st.button("Adicionar")

if adicionar_venda:
    data_adicionar = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    nova_venda = pd.DataFrame({
        'id_vendas': [df_vendas.index.max() + 1],  # Gerando o próximo id_vendas
        'data': [data_adicionar],
        'produto': [valor_produto_filtro],
        'quantidade': [quantidade_adicionado],
        'modo_pagamento': [valor_modo_filtro]
    })
    
    # Concatenar nova venda ao DataFrame df_vendas
    df_vendas = pd.concat([df_vendas, nova_venda], ignore_index=True)
    
    # Atualizar o id_vendas
    atualizar_id_vendas()
    
    # Salva o DataFrame em um arquivo CSV atualizado
    df_vendas.to_csv('dataset/padaria_venda.csv', decimal='.', sep=',', index=True)
    
    # Mostra o DataFrame atualizado na interface
    st.dataframe(df_vendas)

# Módulo 2: Remoção de Vendas
st.markdown('### Remoção de Vendas')

if not df_vendas.empty:
    valor_id_filtro = st.number_input("Selecione o id da venda a ser removida:", 1, df_vendas.index.max())
    remover_venda = st.button("Remover")
    
    if remover_venda:
        df_vendas = df_vendas[df_vendas.index != valor_id_filtro].reset_index(drop=True)
        
        # Atualizar o id_vendas
        atualizar_id_vendas()
        
        # Salva o DataFrame em um arquivo CSV atualizado
        df_vendas.to_csv('dataset/padaria_venda.csv', decimal='.', sep=',', index=True)
        
        # Mostra o DataFrame atualizado na interface
        st.dataframe(df_vendas)
else:
    st.write("Não há vendas para remover.")
