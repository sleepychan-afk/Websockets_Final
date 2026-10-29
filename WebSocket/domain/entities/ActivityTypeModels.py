from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de activityTypes (una fila completa de la tabla)
class ActivityTypeBase(BaseModel):
    activityTypeId: int
    activityTypeName: str
    activityTypeCreationDate: datetime
    activityTypeCreatorId: int
    activityTypeModificationDate: Optional[datetime] = None
    activityTypeModificatorId: Optional[int] = None
    activityTypeEnable: bool

# Modelo para la creacion (Accion 'I')
class ActivityTypeCreate(BaseModel):
    activityTypeName: str
    activityTypeCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class ActivityTypeUpdate(BaseModel):
    activityTypeId: int
    activityTypeName: Optional[str] = None
    activityTypeEnable: Optional[bool] = None
    activityTypeModificatorId: int

# Modelo del listado (Accion 'S')
class LtsActivityTypes(BaseModel):
    activityTypes: List[ActivityTypeBase]
