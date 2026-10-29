from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

# Modelo base de productBacklogItems (una fila completa de la tabla)
class ProductBacklogItemBase(BaseModel):
    PBIId: int
    PBISummary: str
    PBIDescription: str
    PBIsAcceptanceCriteria: str
    PBIOwner: int
    PBIParentLink: int
    PBIStoryPoint: Optional[int] = None
    PBIStartDate: Optional[date] = None
    PBIDueDate: Optional[date] = None
    PBIPriority: Optional[int] = None
    PBICreationDate: datetime
    PBICreatorId: int
    PBIModificationDate: Optional[datetime] = None
    PBIModificatorId: Optional[int] = None
    PBIStatus: int

# Modelo para la creacion (Accion 'I')
class ProductBacklogItemCreate(BaseModel):
    PBISummary: str
    PBIDescription: str
    PBIsAcceptanceCriteria: str
    PBIOwner: int
    PBIParentLink: int
    PBIStoryPoint: Optional[int] = None
    PBIStartDate: Optional[date] = None
    PBIDueDate: Optional[date] = None
    PBIPriority: Optional[int] = None
    PBICreatorId: int
    PBIStatus: int

# Modelo para la actualizacion (Accion 'U')
class ProductBacklogItemUpdate(BaseModel):
    PBIId: int
    PBISummary: Optional[str] = None
    PBIDescription: Optional[str] = None
    PBIsAcceptanceCriteria: Optional[str] = None
    PBIOwner: Optional[int] = None
    PBIParentLink: Optional[int] = None
    PBIStoryPoint: Optional[int] = None
    PBIStartDate: Optional[date] = None
    PBIDueDate: Optional[date] = None
    PBIPriority: Optional[int] = None
    PBIStatus: Optional[int] = None
    PBIModificatorId: int

# Modelo del listado (Accion 'S')
class LtsProductBacklogItems(BaseModel):
    productBacklogItems: List[ProductBacklogItemBase]
