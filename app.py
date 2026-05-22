import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 AI Language Translator")

text = st.text_area("Enter Text")

languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi"
}

target_language = st.selectbox(
    "Select Target Language",
    list(languages.keys())
)

if st.button("Translate"):
    translated = GoogleTranslator(
        source='auto',
        target=languages[target_language]
    ).translate(text)

    st.success("Translated Text:")
    st.write(translated)