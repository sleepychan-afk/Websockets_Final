# WebSocket — API de DB_SCRUM_PLANNING

Estructura igual a la del repo de referencia (`domain/entities`, `infrastructure/database`,
`infrastructure/repositories`), pero con las 12 tablas de `DB_SCRUM_PLANNING` y los
procedimientos almacenados que hicimos.

## Cómo correrlo

```powershell
py -3.13 -m venv venv
.\venv\Scripts\Activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Después abrir **http://127.0.0.1:8000/docs**.

Antes hay que tener ejecutados en SQL Server los scripts `01` al `14` de la carpeta de
procedimientos almacenados.

## Convención de nombres (la misma del repo de referencia)

| Capa | Patrón | Ejemplo |
|---|---|---|
| Modelos | `<Singular>Models.py` | `UserModels.py`, `TaskCommentModels.py` |
| Modelo de fila | `<Singular>Base` | `UserBase` |
| Modelo de alta | `<Singular>Create` | `UserCreate` |
| Modelo de edición | `<Singular>Update` (lleva el id adentro) | `UserUpdate` |
| Modelo de listado | `Lts<Plural>` | `LtsUsers` → `users: List[UserBase]` |
| Repositorio | `<Plural>Repository.py` / `class <Singular>Repository` | `UsersRepository.py` / `UserRepository` |
| Métodos | `insert_<singular>`, `update_<singular>`, `list_<plural>` | `insert_user`, `list_users` |

## Las 12 tablas

| Ruta | Procedimiento | Modelos | Repositorio |
|---|---|---|---|
| `/status` | `[SQM_CATALOGS].[USP_Status]` | `StatusModels.py` | `StatusRepository.py` |
| `/roles` | `[SQM_SECURITY].[USP_Roles]` | `RolModels.py` | `RolesRepository.py` |
| `/users` | `[SQM_SECURITY].[USP_Users]` | `UserModels.py` | `UsersRepository.py` |
| `/businessvalues` | `[SQM_CATALOGS].[USP_BusinessValues]` | `BusinessValueModels.py` | `BusinessValuesRepository.py` |
| `/priorities` | `[SQM_CATALOGS].[USP_Priorities]` | `PriorityModels.py` | `PrioritiesRepository.py` |
| `/activitytypes` | `[SQM_CATALOGS].[USP_ActivityTypes]` | `ActivityTypeModels.py` | `ActivityTypesRepository.py` |
| `/initiatives` | `[SQM_GENERAL].[USP_Initiatives]` | `InitiativeModels.py` | `InitiativesRepository.py` |
| `/epics` | `[SQM_GENERAL].[USP_Epics]` | `EpicModels.py` | `EpicsRepository.py` |
| `/features` | `[SQM_GENERAL].[USP_Features]` | `FeatureModels.py` | `FeaturesRepository.py` |
| `/productbacklogitems` | `[SQM_GENERAL].[USP_ProductBacklogItems]` | `ProductBacklogItemModels.py` | `ProductBacklogItemsRepository.py` |
| `/tasks` | `[SQM_GENERAL].[USP_Tasks]` | `TaskModels.py` | `TasksRepository.py` |
| `/taskcomments` | `[SQM_GENERAL].[USP_TaskComments]` | `TaskCommentModels.py` | `TaskCommentsRepository.py` |

Cada tabla expone 3 endpoints (GET listar, POST insertar, PUT actualizar) = **36 en total**.

## Cómo se leen los códigos

El procedimiento devuelve `@o_Numero` y ese número es el código HTTP de la respuesta.

| Código | Significado |
|---|---|
| 200 | Actualizado o listado correctamente |
| 201 | Registrado correctamente |
| 204 | No hay más registros en esa página (se responde 200 porque 204 no lleva cuerpo) |
| 400 | Falta un dato obligatorio, está repetido o un relacionado no existe |
| 404 | El registro que se quiere actualizar no existe |
| 405 | Acción no válida |
| 500 | Error de SQL |

## Diferencias respecto al repo de referencia (a propósito)

1. **Parámetros de salida.** En el ejemplo se escriben como `@o_Numero = ? OUTPUT`
   pasando un valor de Python; pyodbc no devuelve valores OUT de esa forma y el código
   siempre quedaba en `0`. Aquí se declaran en T-SQL (`DECLARE @num INT, ...`) y se leen
   con un `SELECT` al final, que sí trae el código real.
2. **Nombres de los parámetros de salida.** Nuestros procedimientos usan
   `@o_MensajeTecnico` y `@o_MensajeUsuario`, no `@o_Mensaje`.
3. **Cantidad de parámetros.** En el `update_user` del ejemplo el SQL tiene 8 `?` pero la
   tupla manda 9 valores, y fija `@i_userModificatorId = NULL` aunque después manda el
   valor. Aquí cada `?` tiene su valor en el mismo orden.
4. **Paginación.** La tarea pide `OFFSET`, así que `list_<plural>` recibe
   `page_number` y `rows_per_page` y los manda como `@i_PageNumber` y `@i_RowsPerPage`.
5. **`requirements.txt`.** En el ejemplo dice `pip install fastapi uvicorn pyodbc`, que es
   un comando y falla con `pip install -r`. Aquí va una librería por línea.
6. **Conexión.** El ejemplo usa `ODBC Driver 17` con usuario y contraseña de SQL; aquí va
   `ODBC Driver 18` con `Trusted_Connection=yes` (autenticación de Windows), que es la que
   funciona en nuestra PC. Si se cambia de máquina, se ajusta `connection.py`.
7. **`main.py`.** El repo de referencia no tiene ningún archivo que levante FastAPI, así
   que este se agregó para exponer los endpoints.
8. **Modelos.** Los campos salen de nuestras tablas, por eso `UserBase` incluye
   `userEmail` y el creador va obligatorio. `userPassword` no aparece en `UserBase` porque
   en la tabla está encriptado (`VARBINARY`) y no se devuelve.

Igual que en el ejemplo, los modelos `Lts<Plural>` quedan declarados pero el repositorio
devuelve la lista en `data`. Si se quiere usar `Lts<Plural>` como `response_model` del GET,
se puede conectar después.
