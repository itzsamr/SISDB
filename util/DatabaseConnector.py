import pypyodbc as odbc

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'SAMAR\\MSSQLSERVER01'
DATABASE_NAME = 'SISDB'

class DatabaseConnector:
    def __init__(self, server, database, driver='{SQL Server}', trusted_connection='yes'):
        self.server = server
        self.database = database
        self.driver = driver
        self.trusted_connection = trusted_connection
        self.connection = None
        self.cursor = None

    def open_connection(self):
        try:
            conn_str = f"DRIVER={{{self.driver}}};SERVER={self.server};DATABASE={self.database};Trusted_Connection={self.trusted_connection};"
            self.connection = odbc.connect(conn_str)
            self.cursor = self.connection.cursor()
            print("Connected to SQL Server database")
        except odbc.Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection closed")

# Example usage:
db_connector = DatabaseConnector(server=SERVER_NAME, database=DATABASE_NAME)
db_connector.open_connection()

# Now you can perform database operations using db_connector.cursor

# Don't forget to close the connection when you're done
db_connector.close_connection()





