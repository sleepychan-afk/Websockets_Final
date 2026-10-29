from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

# Modelo base de tasks (una fila completa de la tabla)
class TaskBase(BaseModel):
    taskId: int
    taskSummary: str
    taskDescription: str
    taskOwner: int
    taskParentLink: int
    taskOriginalEstimate: Optional[float] = None
    taskCompletedWork: Optional[float] = None
    taskRemaningWork: Optional[float] = None
    taskStartDate: Optional[date] = None
    taskCompletedDate: Optional[date] = None
    taskDueDate: Optional[date] = None
    taskActivityType: Optional[int] = None
    taskCreationDate: datetime
    taskCreatorId: int
    taskModificationDate: Optional[datetime] = None
    taskModificatorId: Optional[int] = None
    taskStatus: int

# Modelo para la creacion (Accion 'I')
class TaskCreate(BaseModel):
    taskSummary: str
    taskDescription: str
    taskOwner: int
    taskParentLink: int
    taskOriginalEstimate: Optional[float] = None
    taskCompletedWork: Optional[float] = None
    taskRemaningWork: Optional[float] = None
    taskStartDate: Optional[date] = None
    taskCompletedDate: Optional[date] = None
    taskDueDate: Optional[date] = None
    taskActivityType: Optional[int] = None
    taskCreatorId: int
    taskStatus: int

# Modelo para la actualizacion (Accion 'U')
class TaskUpdate(BaseModel):
    taskId: int
    taskSummary: Optional[str] = None
    taskDescription: Optional[str] = None
    taskOwner: Optional[int] = None
    taskParentLink: Optional[int] = None
    taskOriginalEstimate: Optional[float] = None
    taskCompletedWork: Optional[float] = None
    taskRemaningWork: Optional[float] = None
    taskStartDate: Optional[date] = None
    taskCompletedDate: Optional[date] = None
    taskDueDate: Optional[date] = None
    taskActivityType: Optional[int] = None
    taskStatus: Optional[int] = None
    taskModificatorId: int

# Modelo del listado (Accion 'S')
class LtsTasks(BaseModel):
    tasks: List[TaskBase]
