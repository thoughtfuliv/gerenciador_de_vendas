import pandas as pd
import streamlit as st
from utilidades import leitura_de_dados
from datetime import datetime

st.sidebar.markdown("Desenvolvido por [Lívia C.](https://br.linkedin.com/in/l%C3%ADvia-pinheiro-0a7a45201?trk=public_profile_browsemap)")

# Verifica se 'dados' está inicializado em session_state
if 'dados' not in st.session_state:
    st.session_state['dados'] = None

# Função para carregar os dados, ajuste conforme necessário
leitura_de_dados()

# Obtém os DataFrames de vendas e preços do session_state
df_vendas = st.session_state['dados']['df_vendas']
df_precos = st.session_state['dados']['df_precos']

# Se df_vendas for None ou vazio, inicializa com um DataFrame vazio
if df_vendas is None:
    df_vendas = pd.DataFrame(columns=['id_vendas', 'data', 'produto', 'quantidade', 'modo_pagamento'])

# Interface do Streamlit
st.markdown('## 📈 Gestão das Vendas')
st.divider()

st.markdown('### Adição de Vendas')

produto_adicionado = df_precos['produto'].to_list()

valor_produto_filtro = st.selectbox("Selecione o produto vendido:", produto_adicionado)

quantidade_adicionado = st.selectbox("Selecione a quantidade vendida:", [1, 2, 3, 4, 5])

valor_modo_filtro = st.selectbox("Selecione o modo de pagamento:", ["pix", "debito", "credito"])

adicionar_venda = st.button("Adicionar")

if adicionar_venda:
    data_adicionar = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    nova_venda = pd.DataFrame({
        'data': [data_adicionar],
        'produto': [valor_produto_filtro],
        'quantidade': [quantidade_adicionado],
        'modo_pagamento': [valor_modo_filtro]
    })
    
    df_vendas = pd.concat([df_vendas, nova_venda], ignore_index=True)

    # Atualiza o DataFrame no session_state
    st.session_state['dados']['df_vendas'] = df_vendas

    # Salva o DataFrame em um arquivo CSV
    df_vendas.to_csv('C:/Users/paula/Documents/PROJETO_PAINEL_VENDAS/painel_comercial/dataset/padaria_venda.csv', decimal='.', sep=',', index=False)

    # Mostra o DataFrame atualizado na interface
    st.dataframe(df_vendas)


st.markdown('### Remoção de Vendas')

valor_id_filtro = st.number_input("Selecione o id da venda a ser removida:", 0, len(df_vendas)-1)
remover_venda = st.button("Remover")
if remover_venda and valor_id_filtro is not None:
    # Converte o índice para um número inteiro
    indice_remover = int(valor_id_filtro)
    
    # Remove a linha do DataFrame com base no índice selecionado
    df_vendas = df_vendas.drop(index=indice_remover).reset_index(drop=True)
    
    # Salva o DataFrame em um arquivo CSV atualizado
    df_vendas.to_csv('C:/Users/paula/Documents/PROJETO_PAINEL_VENDAS/painel_comercial/dataset/padaria_venda.csv', decimal='.', sep=',', index=False)

    # Mostra o DataFrame atualizado na interface
    st.dataframe(df_vendas)
