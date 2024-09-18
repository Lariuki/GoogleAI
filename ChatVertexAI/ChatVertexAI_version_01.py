from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI

# Use Gemini 1.5 Pro
llm = ChatVertexAI(model="gemini-1.5-pro-001")

# Prepare input for model consumption
pdf_message = {
    "type": "image_url",
    "image_url": {"url": "CAMINHO_URL_GS"},
}

text_message = {
    "type": "text",
    "text": "INSIRA_PERGUNTA",
}

message = HumanMessage(content=[text_message, pdf_message])

# invoke a model response
llm.invoke([message])