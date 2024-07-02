import pandas as pd
import streamlit as st

def leitura_de_dados():
    if st.session_state.dados is None:
        df_precos = pd.read_csv('C:/Users/paula/Documents/PROJETO_PAINEL_VENDAS/painel_comercial/dataset/padaria_preco.csv',decimal ='.',sep=',',index_col=0,parse_dates=True)
        df_vendas = pd.read_csv('C:/Users/paula/Documents/PROJETO_PAINEL_VENDAS/painel_comercial/dataset/padaria_venda.csv',decimal ='.',sep=',',index_col=0,parse_dates=True)
        dados ={'df_vendas':df_vendas,
                'df_precos':df_precos}
        st.session_state['dados']=dados