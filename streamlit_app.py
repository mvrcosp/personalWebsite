#imports
from PIL import Image
import streamlit as st

#loading image
img_marcosp = Image.open("images/marcosp.png")

#page config
st.set_page_config(page_title="MP Personal Page", page_icon=":tada:", layout="wide")

# Introduction
st.title("Oi, Eu sou o Marcos Poleto! :wave:")
st.image(img_marcosp)
st.subheader("Analista de sistemas e aluno da especialização em Data Science e Big Data da UFPR")
st.write("Me interesso bastante no tratamento e manipulação de dados crus para gerar insights ou realizar previsões.")
st.write("Estou construindo essa webpage como entrega final da disciplina de Infraestrutura Computacional 2 do curso DSBD da UFPR.")
st.write("[Meu GitHub >](https://github.com/mvrcosp)")