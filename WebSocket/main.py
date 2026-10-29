from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from domain.entities.StatusModels import StatusCreate, StatusUpdate
from infrastructure.repositories.StatusRepository import StatusRepository
from domain.entities.RolModels import RolCreate, RolUpdate
from infrastructure.repositories.RolesRepository import RolRepository
from domain.entities.UserModels import UserCreate, UserUpdate
from infrastructure.repositories.UsersRepository import UserRepository
from domain.entities.BusinessValueModels import BusinessValueCreate, BusinessValueUpdate
from infrastructure.repositories.BusinessValuesRepository import BusinessValueRepository
from domain.entities.PriorityModels import PriorityCreate, PriorityUpdate
from infrastructure.repositories.PrioritiesRepository import PriorityRepository
from domain.entities.ActivityTypeModels import ActivityTypeCreate, ActivityTypeUpdate
from infrastructure.repositories.ActivityTypesRepository import ActivityTypeRepository
from domain.entities.InitiativeModels import InitiativeCreate, InitiativeUpdate
from infrastructure.repositories.InitiativesRepository import InitiativeRepository
from domain.entities.EpicModels import EpicCreate, EpicUpdate
from infrastructure.repositories.EpicsRepository import EpicRepository
from domain.entities.FeatureModels import FeatureCreate, FeatureUpdate
from infrastructure.repositories.FeaturesRepository import FeatureRepository
from domain.entities.ProductBacklogItemModels import ProductBacklogItemCreate, ProductBacklogItemUpdate
from infrastructure.repositories.ProductBacklogItemsRepository import ProductBacklogItemRepository
from domain.entities.TaskModels import TaskCreate, TaskUpdate
from infrastructure.repositories.TasksRepository import TaskRepository
from domain.entities.TaskCommentModels import TaskCommentCreate, TaskCommentUpdate
from infrastructure.repositories.TaskCommentsRepository import TaskCommentRepository

app = FastAPI(title="DB_SCRUM_PLANNING")


def responder(resultado):
    """Convierte el codigo del procedimiento en el codigo HTTP de la respuesta."""
    codigo = resultado["status_code"] or 500
    if codigo == 204:  # 204 no puede llevar cuerpo
        codigo = 200
    return JSONResponse(status_code=codigo, content=jsonable_encoder(resultado))


status_repository = StatusRepository()
roles_repository = RolRepository()
users_repository = UserRepository()
business_values_repository = BusinessValueRepository()
priorities_repository = PriorityRepository()
activity_types_repository = ActivityTypeRepository()
initiatives_repository = InitiativeRepository()
epics_repository = EpicRepository()
features_repository = FeatureRepository()
product_backlog_items_repository = ProductBacklogItemRepository()
tasks_repository = TaskRepository()
task_comments_repository = TaskCommentRepository()


# ---------------------------- Status ----------------------------
@app.get("/status", tags=["Status"])
def list_status(page_number: int = 1, rows_per_page: int = 10):
    return responder(status_repository.list_status(page_number, rows_per_page))

@app.post("/status", tags=["Status"])
def insert_status(status: StatusCreate):
    return responder(status_repository.insert_status(status))

@app.put("/status", tags=["Status"])
def update_status(status: StatusUpdate):
    return responder(status_repository.update_status(status))

# ---------------------------- Roles ----------------------------
@app.get("/roles", tags=["Roles"])
def list_roles(page_number: int = 1, rows_per_page: int = 10):
    return responder(roles_repository.list_roles(page_number, rows_per_page))

@app.post("/roles", tags=["Roles"])
def insert_rol(rol: RolCreate):
    return responder(roles_repository.insert_rol(rol))

@app.put("/roles", tags=["Roles"])
def update_rol(rol: RolUpdate):
    return responder(roles_repository.update_rol(rol))

# ---------------------------- Users ----------------------------
@app.get("/users", tags=["Users"])
def list_users(page_number: int = 1, rows_per_page: int = 10):
    return responder(users_repository.list_users(page_number, rows_per_page))

@app.post("/users", tags=["Users"])
def insert_user(user: UserCreate):
    return responder(users_repository.insert_user(user))

@app.put("/users", tags=["Users"])
def update_user(user: UserUpdate):
    return responder(users_repository.update_user(user))

# ---------------------------- BusinessValues ----------------------------
@app.get("/businessvalues", tags=["BusinessValues"])
def list_business_values(page_number: int = 1, rows_per_page: int = 10):
    return responder(business_values_repository.list_business_values(page_number, rows_per_page))

@app.post("/businessvalues", tags=["BusinessValues"])
def insert_business_value(business_value: BusinessValueCreate):
    return responder(business_values_repository.insert_business_value(business_value))

@app.put("/businessvalues", tags=["BusinessValues"])
def update_business_value(business_value: BusinessValueUpdate):
    return responder(business_values_repository.update_business_value(business_value))

# ---------------------------- Priorities ----------------------------
@app.get("/priorities", tags=["Priorities"])
def list_priorities(page_number: int = 1, rows_per_page: int = 10):
    return responder(priorities_repository.list_priorities(page_number, rows_per_page))

@app.post("/priorities", tags=["Priorities"])
def insert_priority(priority: PriorityCreate):
    return responder(priorities_repository.insert_priority(priority))

@app.put("/priorities", tags=["Priorities"])
def update_priority(priority: PriorityUpdate):
    return responder(priorities_repository.update_priority(priority))

# ---------------------------- ActivityTypes ----------------------------
@app.get("/activitytypes", tags=["ActivityTypes"])
def list_activity_types(page_number: int = 1, rows_per_page: int = 10):
    return responder(activity_types_repository.list_activity_types(page_number, rows_per_page))

@app.post("/activitytypes", tags=["ActivityTypes"])
def insert_activity_type(activity_type: ActivityTypeCreate):
    return responder(activity_types_repository.insert_activity_type(activity_type))

@app.put("/activitytypes", tags=["ActivityTypes"])
def update_activity_type(activity_type: ActivityTypeUpdate):
    return responder(activity_types_repository.update_activity_type(activity_type))

# ---------------------------- Initiatives ----------------------------
@app.get("/initiatives", tags=["Initiatives"])
def list_initiatives(page_number: int = 1, rows_per_page: int = 10):
    return responder(initiatives_repository.list_initiatives(page_number, rows_per_page))

@app.post("/initiatives", tags=["Initiatives"])
def insert_initiative(initiative: InitiativeCreate):
    return responder(initiatives_repository.insert_initiative(initiative))

@app.put("/initiatives", tags=["Initiatives"])
def update_initiative(initiative: InitiativeUpdate):
    return responder(initiatives_repository.update_initiative(initiative))

# ---------------------------- Epics ----------------------------
@app.get("/epics", tags=["Epics"])
def list_epics(page_number: int = 1, rows_per_page: int = 10):
    return responder(epics_repository.list_epics(page_number, rows_per_page))

@app.post("/epics", tags=["Epics"])
def insert_epic(epic: EpicCreate):
    return responder(epics_repository.insert_epic(epic))

@app.put("/epics", tags=["Epics"])
def update_epic(epic: EpicUpdate):
    return responder(epics_repository.update_epic(epic))

# ---------------------------- Features ----------------------------
@app.get("/features", tags=["Features"])
def list_features(page_number: int = 1, rows_per_page: int = 10):
    return responder(features_repository.list_features(page_number, rows_per_page))

@app.post("/features", tags=["Features"])
def insert_feature(feature: FeatureCreate):
    return responder(features_repository.insert_feature(feature))

@app.put("/features", tags=["Features"])
def update_feature(feature: FeatureUpdate):
    return responder(features_repository.update_feature(feature))

# ---------------------------- ProductBacklogItems ----------------------------
@app.get("/productbacklogitems", tags=["ProductBacklogItems"])
def list_product_backlog_items(page_number: int = 1, rows_per_page: int = 10):
    return responder(product_backlog_items_repository.list_product_backlog_items(page_number, rows_per_page))

@app.post("/productbacklogitems", tags=["ProductBacklogItems"])
def insert_product_backlog_item(product_backlog_item: ProductBacklogItemCreate):
    return responder(product_backlog_items_repository.insert_product_backlog_item(product_backlog_item))

@app.put("/productbacklogitems", tags=["ProductBacklogItems"])
def update_product_backlog_item(product_backlog_item: ProductBacklogItemUpdate):
    return responder(product_backlog_items_repository.update_product_backlog_item(product_backlog_item))

# ---------------------------- Tasks ----------------------------
@app.get("/tasks", tags=["Tasks"])
def list_tasks(page_number: int = 1, rows_per_page: int = 10):
    return responder(tasks_repository.list_tasks(page_number, rows_per_page))

@app.post("/tasks", tags=["Tasks"])
def insert_task(task: TaskCreate):
    return responder(tasks_repository.insert_task(task))

@app.put("/tasks", tags=["Tasks"])
def update_task(task: TaskUpdate):
    return responder(tasks_repository.update_task(task))

# ---------------------------- TaskComments ----------------------------
@app.get("/taskcomments", tags=["TaskComments"])
def list_task_comments(page_number: int = 1, rows_per_page: int = 10):
    return responder(task_comments_repository.list_task_comments(page_number, rows_per_page))

@app.post("/taskcomments", tags=["TaskComments"])
def insert_task_comment(task_comment: TaskCommentCreate):
    return responder(task_comments_repository.insert_task_comment(task_comment))

@app.put("/taskcomments", tags=["TaskComments"])
def update_task_comment(task_comment: TaskCommentUpdate):
    return responder(task_comments_repository.update_task_comment(task_comment))
