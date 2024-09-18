## Objetivo
A intenção desses códigos é para executar testes utilizando como modelo ChatVertexAI e o GenerativeModel. 
A diferença entre esses dois modelos é que o ChatVertexAI é para conversas e GenerativeModel é para criação de conteúdo.

## ChatVertexAI 
# Versão 1: ChatVertexAI Simples 
Este código utiliza o modelo Gemini 1.5 Pro da Vertex AI para processar uma pergunta fornecida pelo usuário e um documento em formato de URL (como um arquivo PDF). O código cria uma mensagem contendo tanto uma pergunta de texto quanto uma URL de um arquivo armazenado no Google Cloud Storage e, em seguida, invoca o modelo para gerar uma resposta.

HumanMessage: Usado para combinar a pergunta e a URL do arquivo.
ChatVertexAI: Invoca o modelo gemini-1.5-pro-001 para gerar uma resposta baseada nas informações fornecidas.
Passos:

Prepara uma mensagem com texto e uma URL de PDF.
Chama o modelo para responder com base nas entradas fornecidas.

# Versão 2: Integração com Google Cloud Storage 
Nesta versão, o código lista todos os arquivos PDF de um bucket do Google Cloud Storage, cria mensagens com as URLs desses arquivos, e em seguida, envia uma pergunta ao modelo Gemini 1.5 Pro junto com essas URLs.

Google Cloud Storage: Utilizado para listar os arquivos PDF no bucket.
Gemini 1.5 Pro: Utilizado para gerar respostas baseadas em uma lista de documentos PDF e uma pergunta.
Passos:

Lista os arquivos PDF de um bucket no Google Cloud.
Combina as URLs dos arquivos com uma pergunta do usuário.
Chama o modelo para fornecer uma resposta.

# Versão 3: Adição de Prompt Personalizado
Esta versão é semelhante à anterior, mas permite a adição de um prompt personalizado que será incluído junto com as URLs dos arquivos PDF e a pergunta do usuário. Isso fornece mais controle sobre o contexto fornecido ao modelo antes de gerar uma resposta.

Prompt Customizado: Adicionado antes de exibir os documentos e a pergunta do usuário.
Google Cloud Storage: Utilizado para listar arquivos e inserir as URLs no conteúdo da mensagem.
Passos:

Lista os arquivos PDF de um bucket.
Insere um prompt customizado e a pergunta do usuário.
Envia tudo para o modelo Gemini 1.5 Pro para gerar uma resposta.

# GenerativeModel
# Versão 1: Utilização do Modelo Generativo Gemini com um PDF
Este código utiliza o modelo generativo Gemini 1.5 Flash da Vertex AI para processar e analisar um arquivo PDF. A funcionalidade principal é fornecer um prompt ao modelo e permitir que ele gere uma resposta com base nas informações fornecidas.

Vertex AI: Inicializa o projeto e carrega o modelo Gemini 1.5 Flash.
PDF: O arquivo PDF é lido a partir de uma URI no Google Cloud Storage.
Prompt: Um prompt personalizado é inserido para orientar a resposta.
Passos:

O projeto Vertex AI é inicializado.
Um arquivo PDF é carregado a partir de uma URL de armazenamento.
O modelo gera uma resposta com base no prompt e no PDF.

# Versão 2: Integração com Google Cloud Storage e Extração de Conteúdo de PDFs
Nesta versão, o código foi expandido para listar e baixar vários arquivos PDF armazenados no Google Cloud Storage. O conteúdo dos arquivos PDF é extraído e usado para fornecer contexto ao modelo Gemini 1.5 Flash junto com a pergunta do usuário.

Google Cloud Storage: O código lista e faz o download dos PDFs armazenados em um bucket, extraindo o conteúdo de cada PDF.
PyPDF2: Usado para ler e extrair texto dos arquivos PDF baixados.
Vertex AI: O modelo Gemini 1.5 Flash gera uma resposta baseada no conteúdo dos PDFs e em uma pergunta fornecida pelo usuário.

Passos:
O conteúdo dos PDFs no bucket do Google Cloud Storage é baixado e lido.
O texto extraído dos PDFs é combinado com um prompt e a pergunta do usuário.
O modelo Gemini 1.5 Flash gera uma resposta usando o conteúdo dos documentos e o prompt.

Diferenças entre as versões:
Versão 1: Processa um único arquivo PDF usando uma URI diretamente.
Versão 2: Lista e baixa todos os PDFs de um bucket no Google Cloud Storage, extrai o texto e envia esse conteúdo para o modelo junto com uma pergunta do usuário.

