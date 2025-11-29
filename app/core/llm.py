from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

llm=ChatGoogleGenerativeAI(model='gemini-2.5-flash',temparature=0)
embedding=GoogleGenerativeAIEmbeddings(model='models/gemini-embedding-001')

def get_gemini():
    return llm

def get_embeddings():
    return embedding