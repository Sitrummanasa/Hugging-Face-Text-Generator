import streamlit as st
from transformers import pipeline
import torch  # Fix for the NameError

st.title("🤗 Hugging Face Text Generator")

user_input = st.text_area("Enter your prompt below:", "Once upon a time")

max_len = st.slider("Max output length", min_value=20, max_value=200, value=50)

if st.button("Generate"):
    with st.spinner("Generating..."):
        generator = pipeline("text-generation", model="gpt2")
        output = generator(user_input, max_length=max_len, num_return_sequences=1)

        st.subheader("Generated Text:")
        st.write(output[0]['generated_text'])
