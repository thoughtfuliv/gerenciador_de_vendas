import pandas as pd
import streamlit as st
from utilidades import leitura_de_dados

st.sidebar.markdown("Desenvolvido por [Lívia C.](https://br.linkedin.com/in/l%C3%ADvia-pinheiro-0a7a45201?trk=public_profile_browsemap)")

# Verifica se 'dados' está inicializado em session_state
#if 'dados' not in st.session_state:
#    st.session_state['dados'] = None

# Função para carregar os dados, ajuste conforme necessário
leitura_de_dados()

# Obtém os DataFrames de vendas e preços do session_state
df_vendas = st.session_state['dados']['df_vendas']
df_precos = st.session_state['dados']['df_precos']

st.dataframe(df_precos)
st.dataframe(df_vendas)
