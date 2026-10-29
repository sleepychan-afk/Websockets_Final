from pydantic import BaseModel
from datetime import datetime, date
from typing import Optional, List

# Modelo base de features (una fila completa de la tabla)
class FeatureBase(BaseModel):
    featureId: int
    featureSummary: str
    featureDescription: str
    featuresAcceptanceCriteria: str
    featureParentLink: int
    featureOwner: int
    featureStartDate: Optional[date] = None
    featureDueDate: Optional[date] = None
    featurePriority: Optional[int] = None
    featureCreationDate: datetime
    featureCreatorId: int
    featureModificationDate: Optional[datetime] = None
    featureModificatorId: Optional[int] = None
    featureStatus: int

# Modelo para la creacion (Accion 'I')
class FeatureCreate(BaseModel):
    featureSummary: str
    featureDescription: str
    featuresAcceptanceCriteria: str
    featureParentLink: int
    featureOwner: int
    featureStartDate: Optional[date] = None
    featureDueDate: Optional[date] = None
    featurePriority: Optional[int] = None
    featureCreatorId: int
    featureStatus: int

# Modelo para la actualizacion (Accion 'U')
class FeatureUpdate(BaseModel):
    featureId: int
    featureSummary: Optional[str] = None
    featureDescription: Optional[str] = None
    featuresAcceptanceCriteria: Optional[str] = None
    featureParentLink: Optional[int] = None
    featureOwner: Optional[int] = None
    featureStartDate: Optional[date] = None
    featureDueDate: Optional[date] = None
    featurePriority: Optional[int] = None
    featureStatus: Optional[int] = None
    featureModificatorId: int

# Modelo del listado (Accion 'S')
class LtsFeatures(BaseModel):
    features: List[FeatureBase]
