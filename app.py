# Import the required libraries
import streamlit as st
from googletrans import Translator

# Function to translate text
def translate_text(text, source_lang, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)
    return translated_text.text

# Main function to create the translation app
def main():
    st.title("Multilingual Text Translation App")

    # Get user input for the text to be translated
    text_to_translate = st.text_area("Enter the text to be translated", height=200)

    # Get user input for the source language
    source_language = st.text_input("Enter the source language (e.g., en for English)")

    # Get user input for the target language
    target_language = st.text_input("Enter the target language (e.g., fr for French)")

    # Translate the text when the user clicks the translate button
    if st.button("Translate"):
        if text_to_translate and source_language and target_language:
            translated_text = translate_text(text_to_translate, source_language, target_language)
            st.write("Translated Text:")
            st.write(translated_text)
        else:
            st.warning("Please enter the text to be translated, source language, and target language.")

# Run the main function
if __name__ == "__main__":
    main()
