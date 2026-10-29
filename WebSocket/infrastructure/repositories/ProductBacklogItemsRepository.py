from infrastructure.database.connection import get_connection
from domain.entities.ProductBacklogItemModels import ProductBacklogItemCreate, ProductBacklogItemUpdate


class ProductBacklogItemRepository:
    def insert_product_backlog_item(self, product_backlog_item: ProductBacklogItemCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_ProductBacklogItems]
                @i_PBISummary = ?,
                @i_PBIDescription = ?,
                @i_PBIsAcceptanceCriteria = ?,
                @i_PBIOwner = ?,
                @i_PBIParentLink = ?,
                @i_PBIStoryPoint = ?,
                @i_PBIStartDate = ?,
                @i_PBIDueDate = ?,
                @i_PBIPriority = ?,
                @i_PBICreatorId = ?,
                @i_PBIStatus = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            product_backlog_item.PBISummary,
            product_backlog_item.PBIDescription,
            product_backlog_item.PBIsAcceptanceCriteria,
            product_backlog_item.PBIOwner,
            product_backlog_item.PBIParentLink,
            product_backlog_item.PBIStoryPoint,
            product_backlog_item.PBIStartDate,
            product_backlog_item.PBIDueDate,
            product_backlog_item.PBIPriority,
            product_backlog_item.PBICreatorId,
            product_backlog_item.PBIStatus,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_product_backlog_item(self, product_backlog_item: ProductBacklogItemUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_ProductBacklogItems]
                @i_PBIId = ?,
                @i_PBISummary = ?,
                @i_PBIDescription = ?,
                @i_PBIsAcceptanceCriteria = ?,
                @i_PBIOwner = ?,
                @i_PBIParentLink = ?,
                @i_PBIStoryPoint = ?,
                @i_PBIStartDate = ?,
                @i_PBIDueDate = ?,
                @i_PBIPriority = ?,
                @i_PBIStatus = ?,
                @i_PBIModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            product_backlog_item.PBIId,
            product_backlog_item.PBISummary,
            product_backlog_item.PBIDescription,
            product_backlog_item.PBIsAcceptanceCriteria,
            product_backlog_item.PBIOwner,
            product_backlog_item.PBIParentLink,
            product_backlog_item.PBIStoryPoint,
            product_backlog_item.PBIStartDate,
            product_backlog_item.PBIDueDate,
            product_backlog_item.PBIPriority,
            product_backlog_item.PBIStatus,
            product_backlog_item.PBIModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_product_backlog_items(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_ProductBacklogItems]
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
