import os
import io
from google.cloud import storage
from PyPDF2 import PdfReader
from vertexai.generative_models import GenerativeModel, Part
from google.cloud import aiplatform

PROJECT_ID = os.getenv("insira_project_id")

# Inicialize o Google Cloud Storage
client = storage.Client()

# Defina o nome do bucket onde os arquivos estão armazenados
bucket_name = 'insira_bucket_name'

# Listar todos os arquivos no bucket
bucket = client.get_bucket(bucket_name)
blobs = bucket.list_blobs()

# Função para baixar e extrair o conteúdo de PDFs do bucket
def get_documents_from_bucket(bucket_name: str) -> list:
    all_text = ""
    for blob in blobs:
        if blob.name.endswith('.pdf'):
            with io.BytesIO(blob.download_as_bytes()) as pdf_file:
                reader = PdfReader(pdf_file)
                for page in reader.pages:
                    all_text += page.extract_text()
    return all_text

# Função que utiliza o modelo generativo e busca nos documentos
def analyze_pdf_and_generate_response(user_question: str):
    # Inicialize o Vertex AI com a região correta
    from vertexai import init
    init(project=PROJECT_ID, location="us-central1")

    # Carregar o modelo Gemini 1.5
    model = GenerativeModel("gemini-1.5-flash-001")

    # Buscar o conteúdo dos PDFs no bucket
    documents_text = get_documents_from_bucket(bucket_name)

    if not documents_text:
        raise Exception("Nenhum conteúdo de PDF encontrado no bucket.")

    # Prompt com as instruções
    prompt = """
    INSIRA_PROMPT
    """

    # Combine o prompt, o conteúdo dos documentos e a pergunta do usuário
    full_context = prompt + "\n\nConteúdo dos documentos:\n" + documents_text + "\n\nPergunta do usuário:\n" + user_question

    # Inserir o conteúdo dos documentos ao lado do prompt e da pergunta
    contents = [Part.from_text(full_context)]

    # Enviar para o modelo e gerar a resposta
    response = model.generate_content(contents)
    print(response.text)
    return response.text

# Função principal que combina tudo
def main():
    # Defina a pergunta do usuário
    user_question = "INSIRA_PERGUNTA"

    # Inicializa o Vertex AI e faz a busca nos documentos, com o prompt separado da pergunta
    analyze_pdf_and_generate_response(user_question)


if __name__ == "__main__":
    main()