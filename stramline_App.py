from bardapi import Bard
from dotenv import load_dotenv

load_dotenv()

def call_bard(query):
    # Replace 'YOUR_API_KEY' with your actual Bard API key
    bard = Bard(token='your_cookie_value')
    answer = bard.get_answer(query)
    return answer['content']

# Example usage
response = call_bard("What movie would you recommend?")
print(response)
#summarizer
def summarizer(query):
    # Replace 'YOUR_API_KEY' with your actual Bard API key
    bard = Bard(token='your_cookie_value')
    answer = bard.get_answer(query)
    return answer['content']

# Example usage
summary = summarizer("On a sunny day, John went to the park to play baseball with his friends. He hit a home run and everyone cheered.")
print(summary)
from googletrans import Translator
from bardapi.core import Bard

def bard_translator(input_text, token, target_language='en'):
    # Create a Bard instance with the provided API key
    bard = Bard(token=token)

    # Get a response from Bard-API
    response = bard.get_answer(input_text)

    # Extract the content from the response
    bard_content = response['content']

    # Create a Translator object
    translator = Translator()

    # Translate the content using Googletrans
    translation = translator.translate(bard_content, dest=target_language)

    return translation.text

# Example usage with your Bard API key
api_key = 'your_cookie_value'
input_text = '''Bonjour, comment vas-tu?'''
translated_text = bard_translator(input_text, token=api_key, target_language='en')

print(translated_text)
#retriver
def retriever(query):
    
    bard = Bard(token='your_cookie_value')
    answer = bard.get_answer(query)
    return answer['content']

# Example usage
input_query = retriever('What is the capital of France?')
print(input_query)
