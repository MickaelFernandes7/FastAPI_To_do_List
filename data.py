from typing import List, Dict, Any, Optional, Union
from enum import Enum

class OpcoesDeStatus(str, Enum):
    a_fazer = "A Fazer"
    fazendo = "Fazendo"
    feito   = "Feito"

Item = Dict[str,Union[int, str, OpcoesDeStatus]]

class AFazer:
    a_fazer: List[Item] = [
        {"id": 1, "titulo": "Estudar", 
        "descricao": "Estudar programação", 
        "status": OpcoesDeStatus.a_fazer},
        {"id": 2, "titulo": "Trabalhar", "descricao": "Construir um sistema programação", "status": OpcoesDeStatus.a_fazer},
        {"id": 3, "titulo": "Treinar", "descricao": "Ir para a academia", "status": OpcoesDeStatus.a_fazer}
    ]
    id_atual = 3

    def listar(self):
        return self.a_fazer   
    
    def inserir(self, item: Item) -> Item:
        self.id_atual += 1
        item["id"] = self.id_atual 
        self.a_fazer.append(item)
        return item 
    
    def pegar_item(self, item_id: int) -> Item:
        item = filter(lambda x: x["id"] == item_id, self.a_fazer)
        return list(item)[0]
    
    def filtrar(self, status: OpcoesDeStatus) -> List[Item]:
        return list(filter(lambda x: x["status"] == status, self.a_fazer))
