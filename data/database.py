from data.database_connection import DatabaseConnection


db = "data\\data.db"


def create_todos_table():
    with DatabaseConnection(db) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS todos(content text, num INTEGER PRIMARY KEY AUTOINCREMENT, done integer);"
        )


def add_todo(content):
    with DatabaseConnection(db) as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO todos VALUES(?, null, 0)", (content,))


def get_all_todos():
    with DatabaseConnection(db) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM todos")
        # it gives us a list of tuples [(content, num, done), (content, num, done)]
        todos = cursor.fetchall()
        # todos = [
        #     {"content": row[0], "num": row[1], "done": row[2]}
        #     for row in cursor.fetchall()
        # ]
    return todos


def mark_todo_as_done(num):
    with DatabaseConnection(db) as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE todos SET done=1 WHERE num=?", (num,))


def mark_todo_as_undone(num):
    with DatabaseConnection(db) as connection:
        cursor = connection.cursor()
        cursor.execute("UPDATE todos SET done=0 WHERE num=?", (num,))


def delete_todo(num):
    with DatabaseConnection(db) as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM todos WHERE num=?", (num,))
