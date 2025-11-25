import streamlit as st
import google.generativeai as genai

# Configurar API
genai.configure(api_key="AIzaSyDcS2tHoy9YgmF2tNT6WOmdoJwby7H4F6Q")

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
            response = model.generate_content(user_input)
            st.subheader("Resultado:")
            st.write(response.text)