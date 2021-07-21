from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from data import OpcoesDeStatus

class ModelodoItem(BaseModel): #Basemodel mostra o schema no swagger
    titulo: str
    status: Optional[OpcoesDeStatus]

class ModelodoItemResposta(ModelodoItem):
    id: int