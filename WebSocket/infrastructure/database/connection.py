import pyodbc

def get_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=DB_SCRUM_PLANNING;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )
