import streamlit as st
import openai

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

# Function to translate text using OpenAI's GPT-3 (using the new API)
def translate_text_with_openai(text, target_language):
  """
  This function translates text using OpenAI's GPT-3 with the updated API.

  Args:
      text: The text to be translated.
      target_language: The target language code (e.g., "fr" for French).

  Returns:
      The translated text.
  """
  response = openai.Completion.create(
      model="gpt-3.5-turbo-instruct", 
      prompt="Translate the following text into " + target_language + ": " + text,
      max_tokens=150,
  )
  translated_text = response.choices[0].text.strip()
  return translated_text

# Main function to create the translation app
def main():
  st.title("Multilingual Text Translation App")

  # Get user input for the text to be translated
  text_to_translate = st.text_area("Enter the text to be translated", height=200)

  # Get user input for the target language
  target_language = st.text_input("Enter the target language (e.g., fr for French)")

  # Translate the text when the user clicks the translate button
  if st.button("Translate"):
    if text_to_translate and target_language:
      translated_text = translate_text_with_openai(text_to_translate, target_language)
      st.write("Translated Text:")
      st.write(translated_text)
    else:
      st.warning("Please enter the text to be translated and the target language.")

# Run the main function
if __name__ == "__main__":
  main()
