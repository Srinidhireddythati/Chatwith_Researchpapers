# Import the required libraries
import streamlit as st
import openai

# Set up the Streamlit app
st.title("Chat with Research Papers 🔎🤖")
st.caption("This app allows you to chat with arXiv research papers using GPT-4.")

# Input field for the OpenAI API key
api_key = st.text_input("Enter your OpenAI API Key", type="password")

# Function to query the OpenAI API
def query_openai(api_key, prompt):
    openai.api_key = api_key  # Set the API key
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use the appropriate model
        messages=[
            {"role": "system", "content": "You are an AI assistant that helps with searching arXiv research papers."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

# Function to search arXiv using OpenAI
def search_arxiv(api_key, query):
    prompt = f"Search arXiv for research papers related to: {query}\n"
    return query_openai(api_key, prompt)

# Get the search query from the user
query = st.text_input("Enter the Search Query", type="default")

if api_key and query:
    # Search arXiv using the AI Assistant
    response = search_arxiv(api_key, query)
    st.write(response)
