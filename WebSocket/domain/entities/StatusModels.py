from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de status (una fila completa de la tabla)
class StatusBase(BaseModel):
    statusId: int
    statusName: str
    statusCreationDate: datetime
    statusCreatorId: int
    statusModificationDate: datetime
    statusModificatorId: Optional[int] = None
    statusEnable: bool

# Modelo para la creacion (Accion 'I')
class StatusCreate(BaseModel):
    statusName: str
    statusCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class StatusUpdate(BaseModel):
    statusId: int
    statusName: Optional[str] = None
    statusEnable: Optional[bool] = None
    statusModificatorId: int

# Modelo del listado (Accion 'S')
class LtsStatus(BaseModel):
    status: List[StatusBase]
