import pandas as pd
import streamlit as st
from datetime import date



def gravar_dados(nome, data_nasc, tipo):
    if nome and dt_nasc <= date.today():
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome}, {data_nasc}, {tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro",
    page_icon="📚"
)

st.title("Cadastros de Clientes")
st.divider()

nome = st.text_input("Digite o Nome do Cliente",
                     key="nome")
dt_nasc = st.date_input("Data De Nacimento", format="DD/MM/YYYY")

tipo =st.selectbox("Tipo de Cliente",
                   ["Pessoa Juridica",
                   "Pessoa Física"])

botao_cadastrar = st.button("Cadastrar",
                            on_click=gravar_dados,
                            args=(nome, dt_nasc, tipo))


if botao_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cadastro Realizado com Sucesso!", icon="👌")
    else:
        st.error("Erro ao tentar cadastrar o cliente!", icon="🚨")

