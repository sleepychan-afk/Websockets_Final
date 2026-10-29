from infrastructure.database.connection import get_connection
from domain.entities.FeatureModels import FeatureCreate, FeatureUpdate


class FeatureRepository:
    def insert_feature(self, feature: FeatureCreate):
        """
        Inserta un registro (Accion 'I').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Features]
                @i_featureSummary = ?,
                @i_featureDescription = ?,
                @i_featuresAcceptanceCriteria = ?,
                @i_featureParentLink = ?,
                @i_featureOwner = ?,
                @i_featureStartDate = ?,
                @i_featureDueDate = ?,
                @i_featurePriority = ?,
                @i_featureCreatorId = ?,
                @i_featureStatus = ?,
                @w_Accion = 'I',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            feature.featureSummary,
            feature.featureDescription,
            feature.featuresAcceptanceCriteria,
            feature.featureParentLink,
            feature.featureOwner,
            feature.featureStartDate,
            feature.featureDueDate,
            feature.featurePriority,
            feature.featureCreatorId,
            feature.featureStatus,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def update_feature(self, feature: FeatureUpdate):
        """
        Actualiza un registro (Accion 'U').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Features]
                @i_featureId = ?,
                @i_featureSummary = ?,
                @i_featureDescription = ?,
                @i_featuresAcceptanceCriteria = ?,
                @i_featureParentLink = ?,
                @i_featureOwner = ?,
                @i_featureStartDate = ?,
                @i_featureDueDate = ?,
                @i_featurePriority = ?,
                @i_featureStatus = ?,
                @i_featureModificatorId = ?,
                @w_Accion = 'U',
                @o_Numero = @num OUTPUT,
                @o_MensajeTecnico = @tec OUTPUT,
                @o_MensajeUsuario = @usu OUTPUT;
            SELECT @num AS Numero, @usu AS Mensaje;
        """, (
            feature.featureId,
            feature.featureSummary,
            feature.featureDescription,
            feature.featuresAcceptanceCriteria,
            feature.featureParentLink,
            feature.featureOwner,
            feature.featureStartDate,
            feature.featureDueDate,
            feature.featurePriority,
            feature.featureStatus,
            feature.featureModificatorId,
        ))

        result = cursor.fetchone()
        conn.commit()
        cursor.close()
        conn.close()

        return {"status_code": result[0], "message": result[1]}

    def list_features(self, page_number: int = 1, rows_per_page: int = 10):
        """
        Lista los registros con paginacion OFFSET (Accion 'S').
        """
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SET NOCOUNT ON;
            DECLARE @num INT, @tec VARCHAR(500), @usu VARCHAR(500);
            EXEC [SQM_GENERAL].[USP_Features]
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
