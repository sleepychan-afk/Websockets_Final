from infrastructure.database.connection import get_connection
from domain.entities.TaskCommentModels import TaskCommentCreate, TaskCommentUpdate


class TaskCommentRepository:
    def insert_task_comment(self, task_comment: TaskCommentCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_TaskComments]
                @i_taskCommentParentLink = ?,
                @i_taskCommentOwner = ?,
                @i_taskCommentText = ?,
                @i_taskCommentCreatorId = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            task_comment.taskCommentParentLink,
            task_comment.taskCommentOwner,
            task_comment.taskCommentText,
            task_comment.taskCommentCreatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_task_comment(self, task_comment: TaskCommentUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_TaskComments]
                @i_taskCommentId = ?,
                @i_taskCommentText = ?,
                @i_taskCommentStatus = ?,
                @i_taskCommentModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            task_comment.taskCommentId,
            task_comment.taskCommentText,
            task_comment.taskCommentStatus,
            task_comment.taskCommentModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_task_comments(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_TaskComments]
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
