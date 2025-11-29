from pydantic import BaseModel

class Default(BaseModel):
    answer:str
class Summary(BaseModel):
    answer:str
    is_legal:bool
class Question(BaseModel):
    question:str