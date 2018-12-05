import pymysql
import os


class DBConnector:

    def __init__(self):
        self.host = os.getenv('mysql_host')
        self.port = int(os.getenv('mysql_port'))
        self.user = os.getenv('mysql_user')
        self.password = os.getenv('mysql_password')
        self.db = 'seafloor_mapping'
        self.charset = 'utf8'

    def connect_mysql(self):
        return pymysql.connect(host=self.host,
                               port=self.port,
                               user=self.user,
                               password=self.password,
                               db=self.db,
                               charset=self.charset)

    def close_mysql(self):
        self.connect_mysql().close()

    def insert_data(self, conn, latitude, longitude, depth, timestamp):
        sql = """insert into data(latitude, longitude, depth, timestamp)
                 values({0},{1},{2},{3})""".format(latitude, longitude, depth, timestamp)
        curs = conn.cursor()
        curs.execute(sql)
        conn.commit()

    def insert_data2(self, conn, latitude, longitude, depth, timestamp):
        sql = """insert into data2(latitude, longitude, depth, timestamp)
                 values({0},{1},{2},{3})""".format(latitude, longitude, depth, timestamp)
        curs = conn.cursor()
        curs.execute(sql)
        conn.commit()

    def select_data(self, conn):
        curs = conn.cursor()
        sql = "select * from data"
        curs.execute(sql)

        return curs.fetchall()

    def select_data2(self, conn):
        curs = conn.cursor()
        sql = "select * from data2"
        curs.execute(sql)

        return curs.fetchall()
