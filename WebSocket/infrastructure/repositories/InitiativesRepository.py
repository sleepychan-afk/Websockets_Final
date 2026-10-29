from infrastructure.database.connection import get_connection
from domain.entities.InitiativeModels import InitiativeCreate, InitiativeUpdate


class InitiativeRepository:
    def insert_initiative(self, initiative: InitiativeCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Initiatives]
                @i_initiativeSummary = ?,
                @i_initiativeDescription = ?,
                @i_initiativeOwner = ?,
                @i_initiativeGoals = ?,
                @i_initiativeBusinessValue = ?,
                @i_initiativeTargetStart = ?,
                @i_initiativeTargetEnd = ?,
                @i_initiativeCreatorId = ?,
                @i_initiativeStatus = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            initiative.initiativeSummary,
            initiative.initiativeDescription,
            initiative.initiativeOwner,
            initiative.initiativeGoals,
            initiative.initiativeBusinessValue,
            initiative.initiativeTargetStart,
            initiative.initiativeTargetEnd,
            initiative.initiativeCreatorId,
            initiative.initiativeStatus,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_initiative(self, initiative: InitiativeUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Initiatives]
                @i_initiativeId = ?,
                @i_initiativeSummary = ?,
                @i_initiativeDescription = ?,
                @i_initiativeOwner = ?,
                @i_initiativeGoals = ?,
                @i_initiativeBusinessValue = ?,
                @i_initiativeTargetStart = ?,
                @i_initiativeTargetEnd = ?,
                @i_initiativeStatus = ?,
                @i_initiativeModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            initiative.initiativeId,
            initiative.initiativeSummary,
            initiative.initiativeDescription,
            initiative.initiativeOwner,
            initiative.initiativeGoals,
            initiative.initiativeBusinessValue,
            initiative.initiativeTargetStart,
            initiative.initiativeTargetEnd,
            initiative.initiativeStatus,
            initiative.initiativeModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_initiatives(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Initiatives]
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
