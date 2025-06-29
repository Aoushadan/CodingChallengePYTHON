from util.db_conn_util import DBConnUtil

def test_db_connection():
    conn = DBConnUtil.get_connection()
    if conn:
        print("DB connection successful!")
        conn.close()
    else:
        print("DB connection failed!")

if __name__ == "__main__":
    test_db_connection()
