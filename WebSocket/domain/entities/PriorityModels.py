from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de priorities (una fila completa de la tabla)
class PriorityBase(BaseModel):
    priorityId: int
    priorityName: str
    priorityCreationDate: datetime
    priorityCreatorId: int
    priorityModificationDate: Optional[datetime] = None
    priorityModificatorId: Optional[int] = None
    priorityEnable: bool

# Modelo para la creacion (Accion 'I')
class PriorityCreate(BaseModel):
    priorityName: str
    priorityCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class PriorityUpdate(BaseModel):
    priorityId: int
    priorityName: Optional[str] = None
    priorityEnable: Optional[bool] = None
    priorityModificatorId: int

# Modelo del listado (Accion 'S')
class LtsPriorities(BaseModel):
    priorities: List[PriorityBase]
