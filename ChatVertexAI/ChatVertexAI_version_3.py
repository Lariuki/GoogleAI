from google.cloud import storage
from langchain_core.messages import HumanMessage
from langchain_google_vertexai import ChatVertexAI

# Inicialize o cliente do Google Cloud Storage
client = storage.Client()

# Defina o nome do bucket onde os arquivos estão armazenados
bucket_name = 'name-bucket

# Listar todos os arquivos no bucket, incluindo subpastas
bucket = client.get_bucket(bucket_name)
blobs = bucket.list_blobs()

# Use Gemini 1.5 Pro
llm = ChatVertexAI(model="gemini-1.5-pro-001")

# Função para criar a mensagem de URL do arquivo PDF a partir de um blob
def create_pdf_message(blob):
    return f"gs://{bucket_name}/{blob.name}"

# Crie uma lista de mensagens com todas as URLs dos arquivos PDF do bucket e suas subpastas
pdf_urls = [create_pdf_message(blob) for blob in blobs if blob.name.endswith('.pdf')]

# Verifica se há arquivos PDF
if not pdf_urls:
    raise Exception("Nenhum arquivo PDF encontrado no bucket.")

# Prepare a mensagem de prompt inicial
prompt_message = """INSIRA_PROMPT"""

# Prepare a pergunta do usuário
user_question = "INSIRA_PERGUNTA"

# Combine o prompt, as URLs dos PDFs e a pergunta do usuário em uma única mensagem
content = prompt_message + "\n\nAqui estão os documentos relevantes:\n" + "\n".join(pdf_urls) + "\n\nPergunta: " + user_question

# Crie uma mensagem do tipo 'HumanMessage'
message = HumanMessage(content=content)

# Invocar o modelo para gerar a resposta
response = llm.invoke([message])

# Exibir a resposta
print(response)