from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

# Modelo base de businessValues (una fila completa de la tabla)
class BusinessValueBase(BaseModel):
    businessValueId: int
    businessValueName: str
    businessValueCreationDate: datetime
    businessValueCreatorId: int
    businessValueModificationDate: Optional[datetime] = None
    businessValueModificatorId: Optional[int] = None
    businessValueEnable: bool

# Modelo para la creacion (Accion 'I')
class BusinessValueCreate(BaseModel):
    businessValueName: str
    businessValueCreatorId: int

# Modelo para la actualizacion (Accion 'U')
class BusinessValueUpdate(BaseModel):
    businessValueId: int
    businessValueName: Optional[str] = None
    businessValueEnable: Optional[bool] = None
    businessValueModificatorId: int

# Modelo del listado (Accion 'S')
class LtsBusinessValues(BaseModel):
    businessValues: List[BusinessValueBase]
