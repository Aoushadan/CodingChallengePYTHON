import pyodbc
from util.db_property_util import get_property_string

class DBConnUtil:
    @staticmethod
    def get_connection():
        props = get_property_string("db.properties")
        if props is None:
            return None
        try:
            server = props['server']
            database = props['database']
            username = props.get('username')
            password = props.get('password')

            if username and password:

                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
                )
            else:

                conn_str = (
                    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                    f"SERVER={server};DATABASE={database};Trusted_Connection=yes"
                )

            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            print(f"[DBConnUtil Error] Failed to connect to DB: {e}")
            return None
