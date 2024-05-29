#imports
from PIL import Image
import streamlit as st

#loading image
img_marcosp = Image.open("images/marcosp.png")
rossmann = Image.open("images/rossmann.png")
customerseg = Image.open("images/cs.png")

def main():
    #page config
    st.set_page_config(page_title="MP Personal Page", page_icon=":tada:", layout="wide")
    # Add tabs to the app
    tabs = ["Sobre Mim", "Projetos", "Contato"]
    choice = st.sidebar.selectbox("Escolha a Aba", tabs)

    if choice == "Sobre Mim":
        about_me()

    elif choice == "Projetos":
        projetos()

    elif choice == "Contato":
        contato()

# About Me
def about_me():
    st.title("Oi, Eu sou o Marcos Poleto! :wave:")
    st.image(img_marcosp)
    st.subheader("Analista de sistemas e aluno da especialização em Data Science e Big Data da UFPR")
    st.write("Me interesso bastante no tratamento e manipulação de dados crus para gerar insights ou realizar previsões.")
    st.write("Estou construindo essa webpage como entrega final da disciplina de Infraestrutura Computacional 2 do curso DSBD da UFPR.")
    st.write("[Meu GitHub >](https://github.com/mvrcosp)")
    

def projetos():
    st.header("Meus Projetos")
    st.write("Aqui estão alguns dos meus projetos no GitHub.")
    #Projeto 1
    st.subheader("[Rossmann - Previsão de Vendas](https://github.com/mvrcosp/Rossmann)")
    col1, col2 = st.columns([1,2])
    with col1:
        st.image(rossmann, use_column_width=True)
    with col2:
        st.write("**Descrição do Projeto**")
        st.write("Previsão total de vendas para cada loja da rede Rossmann durante os próximos 6 meses.")
        st.write("Realizei uma extensa limpeza e manipulação dos dados, criei novos atributos com feature engineering, realizei EDA e testei alguns modelos de ML para construir a previsão.")

    #Projeto 2
    st.subheader("[Segmentação de Clientes](https://github.com/mvrcosp/CustomerSegmentation)")
    col1, col2 = st.columns([1,2])
    with col1:
        st.image(customerseg, use_column_width=True) #caption="Imagem do Projeto 1", )
    with col2:
        st.write("**Descrição do Projeto**")
        st.write("Segmentação de clientes para melhor entender seus comportamentos e planejar campanhas de marketing")
        st.write("Mais uma extensa limpeza e manipulação dos dados, criei novos atributos com feature engineering, realizei EDA e testei modelos de aprendizado não supervisionado para construir grupos similares.")

def contato():
    st.header("Contato")
    st.write("Me manda uma mensagem!")

    # Add contact information
    st.write("Email :email:: marcosffpoleto@gmail.com")
    st.write("Linkedin :man_in_tuxedo:: [>](https://www.linkedin.com/in/marcos-f-f-poleto/)")
    st.write("Instagram :camera_with_flash:: [@mvrcxsfp](https://www.instagram.com/mvrcxsfp/)")

    # Add text box for messages
    st.subheader("Me manda um inbox!")
    message = st.text_area("Digite sua mensagem aqui")

if __name__ == "__main__":
    main()