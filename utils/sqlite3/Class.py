# class Database_SQLITE:
#     def __init__(self, path_to_db="data/keyboards.db"):
#         self.path_to_db = path_to_db
#
#     @property
#     def connection(self):
#         return sqlite3.connect(database=self.path_to_db)
#
#     def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
#         if not parameters:
#             parameters = ()
#         connection = self.connection
#         connection.set_trace_callback(logger)
#         cursor = connection.cursor()
#         data = None
#         cursor.execute(sql, parameters)
#
#         if commit:
#             connection.commit()
#         if fetchall:
#             data = cursor.fetchall()
#         if fetchone:
#             data = cursor.fetchone()
#         connection.close()
#         return data
#
#     def create_table_keyboards(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS Keyboards (
#             id INTEGER NOT NULL,
#             name VARCHAR(255) NOT NULL,
#             title TEXT NOT NULL,
#             photo TEXT NULL,
#             PRIMARY KEY (id)
#         );
#         """
#         self.execute(sql, commit=True)
#
#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join([
#             f"{item} = ?" for item in parameters
#         ])
#         return sql, tuple(parameters.values())
#
#     def add_keyboard(self, name, title, photo: str = None):
#         sql = """
#         INSERT INTO Keyboards(name, title, photo) VALUES(?, ?, ?)
#         """
#         return self.execute(sql, parameters=(name, title, photo), commit=True)
#
#     def select_all_keyboards(self):
#         sql = """
#         SELECT * FROM Keyboards
#         """
#         return self.execute(sql, fetchall=True)
#
#     def select_keyboard(self, **kwargs):
#         sql = "SELECT * FROM Keyboards WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchone=True)
#
#     def count_keyboards(self):
#         return self.execute("SELECT COUNT(*) FROM Keyboards;", fetchone=True)
#
#     def update_keyboard_title(self, name, title):
#         sql = """
#         UPDATE Keyboards SET title=? WHERE name=?
#         """
#         return self.execute(sql, parameters=(name, title), commit=True)
#
#     def delet_keyboards(self):
#         self.execute("DELETE FROM Keyboards WHERE TRUE", commit=True)
import aiosqlite

from utils.misc.logging import logger


class Database_SQLITE:
    def __init__(self, path_to_db="data/keyboards.db"):
        self.path_to_db = path_to_db

    async def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        async with aiosqlite.connect(self.path_to_db) as db:
            await db.set_trace_callback(logger)
            cursor = await db.execute(sql, parameters)
            data = None
            if commit:
                await db.commit()
            if fetchall:
                data = await cursor.fetchall()
            if fetchone:
                data = await cursor.fetchone()
            return data

    async def create_table_keyboards(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Keyboards (
            id INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,
            title TEXT NOT NULL,
            photo TEXT NULL,
            PRIMARY KEY (id)
        );  
        """
        await self.execute(sql, commit=True)

    async def create_table_grant(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Grant_Is_Active (
            grant_id INTEGER NOT NULL,
            is_active INTEGER NOT NULL DEFAULT '0',
            PRIMARY KEY (grant_id)
        );
        """
        await self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    async def add_grant(self, grant_id=1):
        sql = """
         INSERT INTO Grant_Is_Active(grant_id) VALUES(?)
         """
        return await self.execute(sql, parameters=(grant_id,), commit=True)

    async def add_keyboard(self, name, title, photo: str = None):
        sql = """
        INSERT INTO Keyboards(name, title, photo) VALUES(?, ?, ?)
        """
        return await self.execute(sql, parameters=(name, title, photo), commit=True)

    async def select_all_keyboards(self):
        sql = """
        SELECT * FROM Keyboards
        """
        return await self.execute(sql, fetchall=True)

    async def select_keyboard(self, **kwargs):
        sql = "SELECT * FROM Keyboards WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, parameters=parameters, fetchone=True)

    async def select_grant(self, **kwargs):
        sql = "SELECT * FROM Grant_Is_Active WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.execute(sql, parameters=parameters, fetchone=True)

    async def count_keyboards(self):
        return await self.execute("SELECT COUNT(*) FROM Keyboards;", fetchone=True)

    async def update_grant(self, is_active):
        sql = """
        UPDATE Grant_Is_Active SET is_active=? WHERE grant_id='1'
        """
        return await self.execute(sql, parameters=(is_active,), commit=True)

    async def update_keyboard_name(self, name, cours_id):
        sql = """
        UPDATE Keyboards SET name=? WHERE id=?
        """
        return await self.execute(sql, parameters=(name, cours_id), commit=True)

    async def update_keyboard_title(self, title, cours_id):
        sql = """
        UPDATE Keyboards SET title=? WHERE id=?
        """
        return await self.execute(sql, parameters=(title, cours_id), commit=True)

    async def update_keyboard_photo(self, photo, id_courses):
        sql = """
        UPDATE Keyboards SET photo=? WHERE id=?
        """
        return await self.execute(sql, parameters=(photo, id_courses), commit=True)

    async def delete_keyboards(self):
        await self.execute("DELETE FROM Keyboards WHERE TRUE", commit=True)
