import pandas as pd
import streamlit as st

def leitura_de_dados():
    if st.session_state.dados is None:
        df_precos = pd.read_csv('dataset/padaria_preco.csv',decimal ='.',sep=',',index_col=0,parse_dates=True)
        df_vendas = pd.read_csv('dataset/padaria_venda.csv',decimal ='.',sep=',',index_col=0,parse_dates=True)
        dados ={'df_vendas':df_vendas,
                'df_precos':df_precos}
        st.session_state['dados']=dados
        
def logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("https://i.imgur.com/N1uEfmO.png");
                background-repeat: no-repeat;
                background-size: 50%;
                padding-top: 180px;
                padding-bottom: 20px;
                background-position: center 50px;
            }
            [data-testid="stSidebarNav"]::before {
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    
def contatos():
    st.sidebar.markdown( """
    <div style="display: flex; justify-content: center; align-items: center;">
    <p>Desenvolvido por Lívia C.</p>
    </div>""",
    unsafe_allow_html=True)
    
    st.sidebar.markdown(
   """
    <div style="display: flex; justify-content: center; align-items: center;">
    <a href="https://github.com/thoughtfuliv" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="25" style="margin-right: 5px;"></a>
    <a href="https://br.linkedin.com/in/l%C3%ADvia-pinheiro-0a7a45201?trk=public_profile_browsemap" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2428/PNG/512/linkedin_black_logo_icon_147114.png" width="25"></a>
    </div>""",
    unsafe_allow_html=True
)
