from infrastructure.database.connection import get_connection
from domain.entities.EpicModels import EpicCreate, EpicUpdate


class EpicRepository:
    def insert_epic(self, epic: EpicCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Epics]
                @i_epicName = ?,
                @i_epicSummary = ?,
                @i_epicDescription = ?,
                @i_epicParentLink = ?,
                @i_epicOwner = ?,
                @i_epicStartDate = ?,
                @i_epicDueDate = ?,
                @i_epicPriority = ?,
                @i_epicCreatorId = ?,
                @i_epicStatus = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            epic.epicName,
            epic.epicSummary,
            epic.epicDescription,
            epic.epicParentLink,
            epic.epicOwner,
            epic.epicStartDate,
            epic.epicDueDate,
            epic.epicPriority,
            epic.epicCreatorId,
            epic.epicStatus,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_epic(self, epic: EpicUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Epics]
                @i_epicId = ?,
                @i_epicName = ?,
                @i_epicSummary = ?,
                @i_epicDescription = ?,
                @i_epicParentLink = ?,
                @i_epicOwner = ?,
                @i_epicStartDate = ?,
                @i_epicDueDate = ?,
                @i_epicPriority = ?,
                @i_epicStatus = ?,
                @i_epicModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            epic.epicId,
            epic.epicName,
            epic.epicSummary,
            epic.epicDescription,
            epic.epicParentLink,
            epic.epicOwner,
            epic.epicStartDate,
            epic.epicDueDate,
            epic.epicPriority,
            epic.epicStatus,
            epic.epicModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_epics(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Epics]
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
