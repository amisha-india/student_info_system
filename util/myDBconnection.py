# Putting all connection separetly because of the open and close problem of connection for each object

import pyodbc #python open database connection
from util.DBPropertyUtil import PropertyUtil

class DBConnection:
    def __init__(self):
        conn_str = PropertyUtil.get_property_string()
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


# con1 = DBConnection() # new connection
# con2 = DBConnection() # new connection