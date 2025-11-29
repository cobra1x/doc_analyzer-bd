from fastapi import APIRouter,UploadFile,File
from app.Services.save_summarize import add_store
from app.Services.QnA import questions
from app.schemas.schema import Default,Question,Summary
from app.Services.summary import get_summary

router=APIRouter()
pdf_name=None

@router.get('/')
def home():
    return {'message':'Hello guys'}

@router.post('/upload_summarize',response_model=Summary)
def upload_and_summarize(file:UploadFile=File(...)):
    global pdf_name
    pdf_name=file.filename
    with open(f'docs/{file.filename}','wb') as f:
        f.write(file.file.read())
    summary=get_summary(pdf_name)
    if summary!="No relevant legal context found to summarize." and summary != 'No relevant legal context found to summarize.':
        return {
            'answer':summary,
            'is_legal':True
        }
    else:
        return {
            'answer': summary,
            'is_legal':False
        }
    
@router.get('/generate_embeddings')
def generate_embeddings():
    global pdf_name
    try:
        add_store(f'docs/{pdf_name}')
        return {'message':True}
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred : {e}")

@router.post('/QnA',response_model=Default)
def question_answer(question:Question):
    answer=questions(question.question)

    return {"answer":answer}