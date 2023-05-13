import mysql.connector


class DBConnector:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Connected to database:", self.database)
        except mysql.connector.Error as err:
            print("Error connecting to database:", err)

    def disconnect(self):
        self.conn.close()
        print("Disconnected from database:", self.database)
