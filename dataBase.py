import psycopg2
import config

class Database:
    def __init__(self):
        self.connection = psycopg2.connect(
            user=config.USER,
            password=config.PASSWORD,
            host=config.HOST,
            port=config.PORT,
            database=config.DB_NAME
        )
        self.cursor = self.connection.cursor()

    def registerUser(self, time: str, text: str, id: int):
        self.cursor.execute("INSERT INTO users (id, time, text) VALUES  (%s, %s, %s)",
                            (time, text, id))
        self.connection.commit()

    def getUsers(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def getUser(self, id: int):
        self.cursor.execute(f"SELECT * FROM users WHERE id={id}")


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()