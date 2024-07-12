# from typing import Union
#
# import asyncpg
# from asyncpg import Connection
# from asyncpg.pool import Pool
#
# from data import config
#
#
# class Database:
#     def __init__(self):
#         self.pool: Union[Pool, None] = None
#
#     async def create(self):
#         self.pool = await asyncpg.create_pool(
#             user=config.DB_USER,
#             password=config.DB_PASS,
#             host=config.DB_HOST,
#             database=config.DB_NAME,
#         )
#
#     async def execute(
#             self,
#             command,
#             *args,
#             fetch: bool = False,
#             fetchval: bool = False,
#             fetchrow: bool = False,
#             execute: bool = False,
#     ):
#
#         async with self.pool.acquire() as connection:
#             connection: Connection
#             async with connection.transaction():
#                 if fetch:
#                     result = await connection.fetch(command, *args)
#                 elif fetchval:
#                     result = await connection.fetchval(command, *args)
#                 elif fetchrow:
#                     result = await connection.fetchrow(command, *args)
#                 elif execute:
#                     result = await connection.execute(command, *args)
#             return result
#
#     async def create_table_course(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS Joylinks_Courses (
#         order_id SERIAL PRIMARY KEY,
#         course_name VARCHAR(255) NOT NULL,
#         course_status INTEGER NOT NULL DEFAULT '0',
#         added_time BIGINT NOT NULL,
#         received_time BIGINT NULL,
#         tg_id BIGINT NOT NULL
#         );
#         """
#         await self.execute(sql, execute=True)
#
#     async def create_table_answers(self):
#         sql = """
#         CREATE TABLE IF NOT EXISTS Joylinks_Questions (
#         id SERIAL PRIMARY KEY,
#         question_math VARCHAR(255) NULL,
#         correct INTEGER NOT NULL DEFAULT '0',
#         department_position INTEGER NOT NULL DEFAULT '1',
#         correct_math VARCHAR(255) NULL,
#         correct_eng VARCHAR(255) NULL,
#         correct_iq VARCHAR(255) NULL,
#         question_chance INTEGER NOT NULL DEFAULT '1',
#         message_id BIGINT NOT NULL,
#         finish_datetime BIGINT NULL,
#         tg_id BIGINT NOT NULL UNIQUE
#         );
#         """
#         await self.execute(sql, execute=True)
#
#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join(
#             [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
#         )
#         return sql, tuple(parameters.values())
#
#     async def add_user_question(self, questions_id, telegram_id, message_id):
#         sql = "INSERT INTO Joylinks_Questions (questions_id, tg_id, message_id) VALUES($1, $2, $3) returning *"
#         return await self.execute(sql, questions_id, telegram_id, message_id, fetchrow=True)
#
#     async def update_user_question(self, questions_id, telegram_id, message_id):
#         sql = f"UPDATE Joylinks_Questions SET questions_id=$1, message_id=$2 WHERE tg_id=$3"
#         return await self.execute(sql, questions_id, message_id, telegram_id, fetchrow=True)
#
#     async def add_user_courses(self, course_name, added_time, tg_id):
#         sql = "INSERT INTO Joylinks_Courses (course_name, added_time, tg_id) VALUES($1, $2, $3) returning *"
#         return await self.execute(sql, course_name, added_time, tg_id, fetchrow=True)
#
#     async def add_user(self, name, surname, tg_full_name, tg_user_name, region, district,
#                        phone_number, user_datetime, tg_id):
#         sql = "INSERT INTO Joylinks_Users (name, surname, tg_full_name, tg_user_name, region, district, " \
#               "phone_number, user_datetime, tg_id) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9) returning *"
#         return await self.execute(sql, name, surname, tg_full_name, tg_user_name, region, district, phone_number,
#                                   user_datetime, tg_id, fetchrow=True)
#
#     async def select_all_users(self):
#         sql = "SELECT * FROM Joylinks_Users"
#         return await self.execute(sql, fetch=True)
#
#     async def select_all_users_for_xlsx(self):
#         sql = "SELECT id, name, surname, tg_full_name, tg_user_name, region, district, phone_number, " \
#               "total_score, tg_id, is_active FROM Joylinks_Users"
#         return await self.execute(sql, fetch=True)
#
#     async def select_all_courses(self):
#         sql = "SELECT * FROM Joylinks_Courses"
#         return await self.execute(sql, fetch=True)
#
#     async def select_user(self, **kwargs):
#         sql = "SELECT * FROM Joylinks_Users WHERE "
#         sql, parameters = self.format_args(sql, parameters=kwargs)
#         return await self.execute(sql, *parameters, fetchrow=True)
#
#     async def select_admins(self, **kwargs):
#         sql = "SELECT * FROM Joylinks_Users WHERE "
#         sql, parameters = self.format_args(sql, parameters=kwargs)
#         return await self.execute(sql, *parameters, fetch=True)
#
#     async def select_courses(self, **kwargs):
#         sql = "SELECT * FROM Joylinks_Courses WHERE "
#         sql, parameters = self.format_args(sql, parameters=kwargs)
#         return await self.execute(sql, *parameters, fetch=True)
#
#     async def select_user_question(self, **kwargs):
#         sql = "SELECT * FROM Joylinks_Questions WHERE "
#         sql, parameters = self.format_args(sql, parameters=kwargs)
#         return await self.execute(sql, *parameters, fetchrow=True)
#
#     async def count_users(self):
#         sql = "SELECT COUNT(*) FROM Joylinks_Users"
#         return await self.execute(sql, fetchval=True)
#
#     async def update_user_is_info(self, tg_id, is_active=None, is_ban=None, is_superadmin=None, is_admin=None):
#         try:
#             if is_active is not None:
#                 sql = "UPDATE Joylinks_Users SET is_active=$1 WHERE tg_id=$2"
#                 await self.execute(sql, is_active, tg_id)
#             if is_ban is not None:
#                 sql = "UPDATE Joylinks_Users SET is_ban=$1 WHERE tg_id=$2"
#                 await self.execute(sql, is_ban, tg_id)
#             if is_superadmin is not None:
#                 sql = "UPDATE Joylinks_Users SET is_superadmin=$1 WHERE tg_id=$2"
#                 await self.execute(sql, is_superadmin, tg_id)
#             if is_admin is not None:
#                 sql = "UPDATE Joylinks_Users SET is_admin=$1 WHERE tg_id=$2"
#                 await self.execute(sql, is_admin, tg_id)
#             return True
#         except Exception:
#             return False
#
#     async def update_user_course(self, course_status, received_time, order_id):
#         if received_time is None:
#             sql = "UPDATE Joylinks_Courses SET course_status=$1 WHERE order_id=$2"
#             return await self.execute(sql, course_status, order_id, execute=True)
#         else:
#             sql = "UPDATE Joylinks_Courses SET course_status=$1, received_time=$2 WHERE order_id=$3"
#             return await self.execute(sql, course_status, received_time, order_id, execute=True)
#
#     async def update_user_question_math(self, questions_id, question_position, department_position, correct_answer_math,
#                                         telegram_id):
#         sql = "UPDATE Joylinks_Questions SET questions_id=$1, question_position=$2, " \
#               "department_position=$3, correct_math=$4 WHERE tg_id=$5"
#         return await self.execute(sql, questions_id, question_position, department_position, correct_answer_math,
#                                   telegram_id, execute=True)
#
#     async def update_user_question_eng(self, questions_id, question_position, department_position, correct_eng,
#                                        telegram_id):
#         sql = "UPDATE Joylinks_Questions SET questions_id=$1, question_position=$2, " \
#               "department_position=$3, correct_eng=$4 WHERE tg_id=$5"
#         return await self.execute(sql, questions_id, question_position, department_position, correct_eng,
#                                   telegram_id, execute=True)
#
#     async def update_user_question_position(self, question_position, department_position,
#                                             correct_answer_eng, telegram_id):
#         sql = "UPDATE Joylinks_Questions SET question_position=$1, department_position=$2, " \
#               "correct_eng=$3 WHERE tg_id=$4"
#         return await self.execute(sql, question_position, department_position,
#                                   correct_answer_eng, telegram_id, execute=True)
#
#     async def update_user_question_iq(self, question_position, department_position, correct_iq, tg_id):
#         sql = "UPDATE Joylinks_Questions SET question_position=$1, department_position=$2, correct_iq=$3 WHERE tg_id=$4"
#         return await self.execute(sql, question_position, department_position, correct_iq, tg_id, execute=True)
#
#     async def update_user_question_score(self, math_score, eng_score, iq_score, total_score, finish_datetime,
#                                          tg_id):
#         sql = "UPDATE Joylinks_Users SET math_score=$1, eng_score=$2, iq_score=$3, total_score=$4 WHERE tg_id=$5"
#         sql_2 = "UPDATE Joylinks_Questions SET finish_datetime=$1 WHERE tg_id=$2"
#         await self.execute(sql, math_score, eng_score, iq_score, total_score, tg_id, execute=True)
#         return await self.execute(sql_2, finish_datetime, tg_id, execute=True)
#
#     async def update_user_info(self, name, surname, region, district, phone_number, tg_id):
#         try:
#             if name is not None:
#                 sql = "UPDATE Joylinks_Users SET name=$1 WHERE tg_id=$2"
#                 info_user = name
#                 await self.execute(sql, info_user, tg_id, execute=True)
#             if surname is not None:
#                 sql = "UPDATE Joylinks_Users SET surname=$1 WHERE tg_id=$2"
#                 info_user = surname
#                 await self.execute(sql, info_user, tg_id, execute=True)
#             if region is not None:
#                 sql = "UPDATE Joylinks_Users SET region=$1 WHERE tg_id=$2"
#                 info_user = region
#                 await self.execute(sql, info_user, tg_id, execute=True)
#             if district is not None:
#                 sql = "UPDATE Joylinks_Users SET district=$1 WHERE tg_id=$2"
#                 info_user = district
#                 await self.execute(sql, info_user, tg_id, execute=True)
#             if phone_number is not None:
#                 sql = "UPDATE Joylinks_Users SET phone_number=$1 WHERE tg_id=$2"
#                 info_user = phone_number
#                 await self.execute(sql, info_user, tg_id, execute=True)
#             return True
#         except Exception as _err:
#             return False
#
#     async def delete_users(self):
#         await self.execute("DELETE FROM Joylinks_Users WHERE True", execute=True)
#
#     async def drop_users(self):
#         await self.execute("DROP TABLE Joylinks_Users", execute=True)
