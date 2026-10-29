from infrastructure.database.connection import get_connection
from domain.entities.TaskModels import TaskCreate, TaskUpdate


class TaskRepository:
    def insert_task(self, task: TaskCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Tasks]
                @i_taskSummary = ?,
                @i_taskDescription = ?,
                @i_taskOwner = ?,
                @i_taskParentLink = ?,
                @i_taskOriginalEstimate = ?,
                @i_taskCompletedWork = ?,
                @i_taskRemaningWork = ?,
                @i_taskStartDate = ?,
                @i_taskCompletedDate = ?,
                @i_taskDueDate = ?,
                @i_taskActivityType = ?,
                @i_taskCreatorId = ?,
                @i_taskStatus = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            task.taskSummary,
            task.taskDescription,
            task.taskOwner,
            task.taskParentLink,
            task.taskOriginalEstimate,
            task.taskCompletedWork,
            task.taskRemaningWork,
            task.taskStartDate,
            task.taskCompletedDate,
            task.taskDueDate,
            task.taskActivityType,
            task.taskCreatorId,
            task.taskStatus,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_task(self, task: TaskUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Tasks]
                @i_taskId = ?,
                @i_taskSummary = ?,
                @i_taskDescription = ?,
                @i_taskOwner = ?,
                @i_taskParentLink = ?,
                @i_taskOriginalEstimate = ?,
                @i_taskCompletedWork = ?,
                @i_taskRemaningWork = ?,
                @i_taskStartDate = ?,
                @i_taskCompletedDate = ?,
                @i_taskDueDate = ?,
                @i_taskActivityType = ?,
                @i_taskStatus = ?,
                @i_taskModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            task.taskId,
            task.taskSummary,
            task.taskDescription,
            task.taskOwner,
            task.taskParentLink,
            task.taskOriginalEstimate,
            task.taskCompletedWork,
            task.taskRemaningWork,
            task.taskStartDate,
            task.taskCompletedDate,
            task.taskDueDate,
            task.taskActivityType,
            task.taskStatus,
            task.taskModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_tasks(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Tasks]
                @i_PageNumber = ?,
                @i_RowsPerPage = ?,
                @w_Accion = 'S',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            page_number,
            rows_per_page,
        ))

        data = []
        if cursor.description[0][0] != "Numero":
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in cursor.fetchall()]
            cursor.nextset()

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1], "data": data}
