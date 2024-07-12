from data.config import SQL_DB_NAME, SQL_TABEL_NAME_2
from utils.time_samarkand.TIME import date_time_now


def get_db_kurs_info_bot():
    import sqlite3
    connect = sqlite3.connect(f'{SQL_DB_NAME}.db')
    cursor = connect.cursor()
    sql_command = (f"""CREATE TABLE IF NOT EXISTS {SQL_TABEL_NAME_2} (
        kurs_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL DEFAULT (12345678),
        name TEXT NOT NULL DEFAULT none,
        surname TEXT NOT NULL DEFAULT none,
        phone_number INTEGER NOT NULL DEFAULT (0),
        location TEXT NOT NULL DEFAULT none,
        user_name TEXT NOT NULL DEFAULT none,
        nick_name TEXT NOT NULL DEFAULT none,
        kurs_date_time TEXT NOT NULL DEFAULT "0000-00-00 00:00:00",
        course_name TEXT NOT NULL DEFAULT none,
        course_status INTEGER NOT NULL DEFAULT (0)
        );""")
    cursor.execute(sql_command)
    # connect.commit()
    return connect, cursor


async def save_info_kurs_db(user_id: int, name: str, surname: str, phone_number: int, location: str, user_name: str,
                            nick_name: str, course_name: str):
    import sqlite3
    kurs_date_time = await date_time_now()
    connect = sqlite3.connect(f'{SQL_DB_NAME}.db')
    cursor = connect.cursor()
    try:
        sql_command = (f"""CREATE TABLE IF NOT EXISTS {SQL_TABEL_NAME_2} (
        kurs_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL DEFAULT (12345678),
        name TEXT NOT NULL DEFAULT none,
        surname TEXT NOT NULL DEFAULT none,
        phone_number INTEGER NOT NULL DEFAULT (0),
        location TEXT NOT NULL DEFAULT none,
        user_name TEXT NOT NULL DEFAULT none,
        nick_name TEXT NOT NULL DEFAULT none,
        kurs_date_time TEXT NOT NULL DEFAULT "0000-00-00 00:00:00",
        course_name TEXT NOT NULL DEFAULT none,
        course_status INTEGER NOT NULL DEFAULT (0)
        );""")
        cursor.execute(sql_command)
        connect.commit()
        cursor.execute(
            f"INSERT INTO {SQL_TABEL_NAME_2} (user_id, name, surname, phone_number, location, user_name, "
            f"nick_name, kurs_date_time, course_name) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, name, surname, phone_number, location, user_name, nick_name, kurs_date_time, course_name))
        connect.commit()
        finish_send = True
    except:
        finish_send = False
    finally:
        cursor.close()
        connect.close()
    return finish_send


async def update_info_kurs_db(kurs_id: int):
    import sqlite3
    connect = sqlite3.connect(f'{SQL_DB_NAME}.db')
    cursor = connect.cursor()
    try:
        sql_command = (f"""CREATE TABLE IF NOT EXISTS {SQL_TABEL_NAME_2} (
        kurs_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL DEFAULT (12345678),
        name TEXT NOT NULL DEFAULT none,
        surname TEXT    NOT NULL DEFAULT none,
        phone_number INTEGER NOT NULL DEFAULT (0),
        location TEXT NOT NULL DEFAULT none,
        user_name TEXT NOT NULL DEFAULT none,
        nick_name TEXT NOT NULL DEFAULT none,
        kurs_date_time TEXT NOT NULL DEFAULT "0000-00-00 00:00:00",
        course_name TEXT NOT NULL DEFAULT none,
        course_status INTEGER NOT NULL DEFAULT (0)
        );""")
        cursor.execute(sql_command)
        connect.commit()
        cursor.execute(f"UPDATE {SQL_TABEL_NAME_2} SET course_status=1 WHERE kurs_id={kurs_id}")
        connect.commit()
        finish_send = True
    except:
        finish_send = False
    finally:
        cursor.close()
        connect.close()
    return finish_send
