import sqlite3


DB_NAME = 'sqlite.db'


def _fetch_all_sql(sql):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    records = cur.execute(sql).fetchall()
    con.close()

    return records


def _execute_sql(sql):
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()

    cur.execute(sql)
    con.commit()
    con.close()


class DB:

    def fetch_all(self, sql):
        return _fetch_all_sql(sql)

    def execute(self, sql):
        return _execute_sql(sql)
