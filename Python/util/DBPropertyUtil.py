def load_db_properties():
    server_name = "SAMAR\MSSQLSERVER01"
    database_name = "SISDB"
    properties = {
        "server": server_name,
        "database": database_name,
        "driver": "{SQL Server}",
    }
    return properties
