from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage
from app.templates.system_prompt import system_prompt
from app.core.llm import get_gemini
from langchain_classic.chains.retrieval import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from app.Services.save_summarize import get_retriever,ai_history

prompt=ChatPromptTemplate.from_messages(
    [
        ('system',system_prompt),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human','Question : {input}')
    ]
)
llm=get_gemini()

doc_chain=create_stuff_documents_chain(llm,prompt)

def questions(question:str)->str:
    retriever=get_retriever()
    retrieval_chain=create_retrieval_chain(retriever,doc_chain)
    result=retrieval_chain.invoke({
        "input":question,
        "chat_history":ai_history
    })
    if result['answer'] != 'No relevant legal context found to answer.' and result['answer'] != "No relevant legal context found to answer.":
        ai_history.append(AIMessage(content=result['answer']))

    return result['answer']