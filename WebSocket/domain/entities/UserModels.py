from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de users (una fila completa de la tabla)
class UserBase(BaseModel):
    userId: int
    userFullName: str
    userName: str
    userEmail: str
    userRolId: int
    userCreationDate: datetime
    userCreatorId: int
    userModificationDate: datetime
    userModificatorId: Optional[int] = None
    userEnable: bool

# Modelo para la creacion (Accion 'I')
class UserCreate(BaseModel):
    userFullName: str
    userName: str
    userEmail: str
    userPassword: str
    userRolId: int
    userCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class UserUpdate(BaseModel):
    userId: int
    userFullName: Optional[str] = None
    userName: Optional[str] = None
    userEmail: Optional[str] = None
    userPassword: Optional[str] = None
    userRolId: Optional[int] = None
    userEnable: Optional[bool] = None
    userModificatorId: int

# Modelo del listado (Accion 'S')
class LtsUsers(BaseModel):
    users: List[UserBase]
