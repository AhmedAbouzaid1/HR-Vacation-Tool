import mysql.connector


class QueryExecutor:
    def __init__(self, conn):
        self.conn = conn

    def selection_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print("Error executing query:", err)

    def update_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            result = self.conn.commit()
            cursor.close()
            return result
        except mysql.connector.Error as err:
            print("Error executing query:", err)
