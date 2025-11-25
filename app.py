import streamlit as st
import google.generativeai as genai

# Configurar API
api_key = st.secrets["API_KEY"]

# Configurando a API
genai.configure(api_key=api_key)

# Criar modelo
model = genai.GenerativeModel("models/gemini-2.5-flash")

# UI do Streamlit
st.title("🍽️ Gerador de Receitas com IA")
st.write("Digite os ingredientes e receba uma receita completa!")

user_input = st.text_input("Digite seu prompt (ingredientes)")

if st.button("Gerar Resposta"):
    if not user_input.strip():
        st.warning("Por favor, digite pelo menos um ingrediente.")
    else:
        with st.spinner("Gerando sua receita..."):
            response = model.generate_content(f"Como chefe 5 estrelas de um mega restaurante famoso , me cite 3 receitas boas para fazer com os meus ingredientes na geladeira : {user_input}, e além dos ingredientes que usarei, proporcionalize indicando quantas gramas / ml de cada ingrediente vai usar, e o modo de preparo, EXEMPLO : ingredientes = [farinha, leite, ovo, frango, queijo] -> coxinha de frango recheada com queijo \n 300g de farinha, 2 ovos, 200ml de leite, 2 fatias de queijo , 300g de frango \n Modo de preparo -> bata a farinha, ovo , leite e sove a massa até ficar numa consistência boa ...")
            st.subheader("Resultado:")
            st.write(response.text)
