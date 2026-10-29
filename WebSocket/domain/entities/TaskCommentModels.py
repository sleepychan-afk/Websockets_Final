from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de taskComments (una fila completa de la tabla)
class TaskCommentBase(BaseModel):
    taskCommentId: int
    taskCommentParentLink: int
    taskCommentOwner: int
    taskCommentText: str
    taskCommentCreationDate: datetime
    taskCommentCreatorId: int
    taskCommentModificationDate: Optional[datetime] = None
    taskCommentModificatorId: Optional[int] = None
    taskCommentStatus: bool

# Modelo para la creacion (Accion 'I')
class TaskCommentCreate(BaseModel):
    taskCommentParentLink: int
    taskCommentOwner: int
    taskCommentText: str
    taskCommentCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class TaskCommentUpdate(BaseModel):
    taskCommentId: int
    taskCommentText: Optional[str] = None
    taskCommentStatus: Optional[bool] = None
    taskCommentModificatorId: int

# Modelo del listado (Accion 'S')
class LtsTaskComments(BaseModel):
    taskComments: List[TaskCommentBase]
