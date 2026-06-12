# Commented out IPython magic to ensure Python compatibility.
# %pip install -U langchain
# %pip install -U langgraph
# %pip install -U google-generativeai
# %pip install -U langchain-google-genai
# %pip install -U langchain-community
# %pip install arxiv

import os
import google.generativeai as genai
from google.colab import userdata

api_key = userdata.get("GEMINI_API_KEY")
os.environ["GOOGLE_API_KEY"] = api_key
genai.configure(api_key=api_key)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.prompts import PromptTemplate

modelo_de_prompt = PromptTemplate(
    template="Explica de manera clara y actualizada cuáles son los impactos de la inteligencia artificial en el área de {tema}.",
    input_variables=["tema"],
)

from langchain_core.output_parsers import StrOutputParser

cadena = modelo_de_prompt | llm | StrOutputParser()

respuesta = cadena.invoke({"tema": "educación"})

print(respuesta)
