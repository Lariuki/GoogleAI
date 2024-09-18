import os

PROJECT_ID = os.getenv("insira_project_id")


def analyze_pdf() -> str:
    # [START generativeaionvertexai_gemini_pdf]
    import vertexai

    from vertexai.generative_models import GenerativeModel, Part

    # TODO(developer): Update project_id and location
    vertexai.init(project=PROJECT_ID, location="us-central1")

    model = GenerativeModel("gemini-1.5-flash-001")

    prompt = """
    INSIRA_PROMPT_PERGUNTA
    """

    pdf_file = Part.from_uri(
        uri="caminho_url_gs",
        mime_type="application/pdf",
    )
    contents = [pdf_file, prompt]

    response = model.generate_content(contents)
    print(response.text)
    # [END generativeaionvertexai_gemini_pdf]

    return response.text


if __name__ == "__main__":
    analyze_pdf()