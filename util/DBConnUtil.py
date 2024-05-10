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
