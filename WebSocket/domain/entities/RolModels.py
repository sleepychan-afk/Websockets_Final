from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de roles (una fila completa de la tabla)
class RolBase(BaseModel):
    rolId: int
    rolName: str
    rolCreationDate: datetime
    rolCreatorId: int
    rolModificationDate: datetime
    rolModificatorId: Optional[int] = None
    rolEnable: bool

# Modelo para la creacion (Accion 'I')
class RolCreate(BaseModel):
    rolName: str
    rolCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class RolUpdate(BaseModel):
    rolId: int
    rolName: Optional[str] = None
    rolEnable: Optional[bool] = None
    rolModificatorId: int

# Modelo del listado (Accion 'S')
class LtsRoles(BaseModel):
    roles: List[RolBase]
