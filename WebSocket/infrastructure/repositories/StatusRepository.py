from infrastructure.database.connection import get_connection
from domain.entities.StatusModels import StatusCreate, StatusUpdate


class StatusRepository:
    def insert_status(self, status: StatusCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_CATALOGS].[USP_Status]
                @i_statusName = ?,
                @i_statusCreatorId = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            status.statusName,
            status.statusCreatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_status(self, status: StatusUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_CATALOGS].[USP_Status]
                @i_statusId = ?,
                @i_statusName = ?,
                @i_statusEnable = ?,
                @i_statusModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            status.statusId,
            status.statusName,
            status.statusEnable,
            status.statusModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_status(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_CATALOGS].[USP_Status]
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
