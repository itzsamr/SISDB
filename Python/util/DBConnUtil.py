import pyodbc
from DBPropertyUtil import load_db_properties


def create_connection():
    properties = load_db_properties()
    conn_str = (
        f"DRIVER={properties['driver']};"
        f"SERVER={properties['server']};"
        f"DATABASE={properties['database']};"
        f"Trusted_Connection=yes;"
    )
    conn = pyodbc.connect(conn_str)
    return conn


def check_db_connection():
    try:
        properties = load_db_properties()
        conn_str = (
            f"DRIVER={properties['driver']};"
            f"SERVER={properties['server']};"
            f"DATABASE={properties['database']};"
            f"Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(conn_str)
        print("Database connection successful!")
        conn.close()
    except Exception as e:
        print(f"Failed to connect to the database: {e}")


# Call the function to check the database connection
check_db_connection()
