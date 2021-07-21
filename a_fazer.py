from fastapi import APIRouter
from typing import List, Dict, Any, Optional
from data import AFazer, OpcoesDeStatus
from modelos import ModelodoItem, ModelodoItemResposta

router = APIRouter()
a_fazer = AFazer

@router.get("/", response_model=List[ModelodoItemResposta])
def listar_a_fazer(status: Optional[OpcoesDeStatus] = None): 
    "View que retorna lista de items a fazer"
    if status is not None:
        return a_fazer.filtrar(status=status)
    return a_fazer.listar()

@router.post("/", response_model=ModelodoItemResposta, status_code=201)
def inserir_a_fazer(item_a_inserir: ModelodoItem): 
    "View que insere item na lista de items a fazer"
    return a_fazer.inserir(item_a_inserir.dict())


@router.get("/{id_do_item}", response_model=ModelodoItemResposta)
def pegar_item_a_fazer(id_do_item: int): 
    "View que mostra um item a partir do ID dele"
    return a_fazer.pegar_item(id_do_item)