from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

# Modelo base de epics (una fila completa de la tabla)
class EpicBase(BaseModel):
    epicId: int
    epicName: str
    epicSummary: str
    epicDescription: str
    epicParentLink: int
    epicOwner: int
    epicStartDate: Optional[date] = None
    epicDueDate: Optional[date] = None
    epicPriority: Optional[int] = None
    epicCreationDate: datetime
    epicCreatorId: int
    epicModificationDate: Optional[datetime] = None
    epicModificatorId: Optional[int] = None
    epicStatus: int

# Modelo para la creacion (Accion 'I')
class EpicCreate(BaseModel):
    epicName: str
    epicSummary: str
    epicDescription: str
    epicParentLink: int
    epicOwner: int
    epicStartDate: Optional[date] = None
    epicDueDate: Optional[date] = None
    epicPriority: Optional[int] = None
    epicCreatorId: int
    epicStatus: int

# Modelo para la actualizacion (Accion 'U')
class EpicUpdate(BaseModel):
    epicId: int
    epicName: Optional[str] = None
    epicSummary: Optional[str] = None
    epicDescription: Optional[str] = None
    epicParentLink: Optional[int] = None
    epicOwner: Optional[int] = None
    epicStartDate: Optional[date] = None
    epicDueDate: Optional[date] = None
    epicPriority: Optional[int] = None
    epicStatus: Optional[int] = None
    epicModificatorId: int

# Modelo del listado (Accion 'S')
class LtsEpics(BaseModel):
    epics: List[EpicBase]
