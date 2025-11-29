from pypdf import PdfReader
from app.core.llm import get_gemini
from langchain_core.prompts import PromptTemplate
from app.templates.summary_prompt import summary_prompt

def get_summary(path):
    reader=PdfReader(f'docs/{path}')
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    prompt=PromptTemplate.from_template(summary_prompt)

    formatted_prmpt=prompt.format(text=text)
    response=get_gemini().invoke(formatted_prmpt)

    return response.content