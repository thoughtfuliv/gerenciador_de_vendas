# Importando as bibliotecas necessárias
import streamlit as st 
import utilidades
from streamlit_carousel import carousel

# comando para startar o webapp: streamlit run 'C:/Users/paula/Documents/PROJETO_PAINEL_VENDAS/painel_comercial/01_Página_Inicial.py'

# Importando logo na sidebar
utilidades.logo()

# Interface do webapp:

st.markdown("## Comece por aqui!")
st.divider()

st.markdown( """
    Este projeto visa facilitar o <strong>gerenciamento e análise de vendas</strong> de um negócio do ramo alimentício, uma padaria chamada de Padaria Sonho.

    O conjunto de dados analisado foi gerado por meio de um script e todos os códigos estão disponíveis no meu repositório GitHub!

    Confira abaixo todas as tecnologias utilizadas neste projeto:
""",unsafe_allow_html=True)

# Carrossel de imagens:

items = [
    dict(
        title=" ",
        text="Linguagem de programação utilizada",
        img="https://cdn.icon-icons.com/icons2/2415/PNG/512/python_original_wordmark_logo_icon_146382.png",
    ),
    dict(
        title="  ",
        text="Manipulação de dados em tabelas",
        img="https://i.imgur.com/70h3JXo.png",
    ),
    dict(
        title="    ",
        text="Geração de gráficos",
        img="https://i.imgur.com/9OPDWkV.png",
    ),
    dict(
        title="    ",
        text="Criação da Interface (WebApp Interativo)",
        img="https://i.imgur.com/oXW1UvW.png",
    ),
        dict(
        title="      ",
        text="Estilização do WebApp",
        img="https://i.imgur.com/ziJzWL8.png",
    ),
]

carousel(items=items,fade=True, width=0.65, container_height= 400)

st.divider()

# Rodapé da página:

st.markdown( """
    <div style="display: flex; justify-content: center; align-items: center;">
    <p>Que tal trocarmos uma ideia?</p>
    </div>""",
    unsafe_allow_html=True)

st.markdown(
   """
    <div style="display: flex; justify-content: center; align-items: center;">
    <a href="https://github.com/thoughtfuliv" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="25" style="margin-right: 5px;"></a>
    <a href="https://br.linkedin.com/in/l%C3%ADvia-pinheiro-0a7a45201?trk=public_profile_browsemap" target="_blank"><img src="https://cdn.icon-icons.com/icons2/2428/PNG/512/linkedin_black_logo_icon_147114.png" width="25"></a>
    </div>""",
    unsafe_allow_html=True
)




