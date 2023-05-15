import pymysql
import time


class create_newuser_medicaldb:  # 创建连接MYSQL的类
    def __init__(self, username, host, db, passwd, newuser_info):
        self.newuser_info = newuser_info
        self.username = username
        self.host = host
        self.db = db
        self.passwd = passwd
        self.conn = self.conn_mysql()
        # sql语句初始化
        self.sql = "INSERT INTO users_personal(name,  tel, " + \
                   "email_address, gender, birthdate, job) Values("

    def conn_mysql(self):  # 创建数据库连接
        conn = pymysql.connect(user=self.username, host=self.host, db=self.db, password=self.passwd, autocommit=True)
        print("----------Mysql is Opened----------")
        return conn

    def close_mysql(self):  # 关闭数据库, 有提示消息
        self.conn.close()
        print("----------Mysql is Closed----------")

    def info2_medicalDB(self):  # 与mysql进行交互,连接medicaldb数据库, 把新用户信息写进users表中
        cur = self.conn.cursor()
        print(666)

        self.sql += "'{}', '{}', '{}', '{}', '{}', '{}'); "\
                    .format(self.newuser_info["name"], self.newuser_info["telephone"],
                            self.newuser_info["email"], self.newuser_info["gender"],
                            self.newuser_info["Birthdate"], self.newuser_info["job"])
        cur.execute(self.sql)
        result = cur.fetchall()
        print(result)
        self.sql = "INSERT INTO users(username, password, " + \
                   " name, creation_date) Values("
        self.sql += " '{}', '{}', '{}', '{}'); "\
                    .format(
                            self.newuser_info["username"], self.newuser_info["password"],
                            self.newuser_info["name"], str(time.asctime())
                            )
        cur.execute(self.sql)
        result = cur.fetchall()
        print(result)
        cur.execute("COMMIT;")
        print("^_^The new user is registered successfully ！username：" + self.newuser_info["username"])

        cur.close()
        self.close_mysql()


def newuser_info2medicaldb(newuser_info):
    print(newuser_info["username"])
    mysql = create_newuser_medicaldb('root', '127.0.0.1', 'medicaldb', 'tzh2002315', newuser_info)  # 创建creator_Mysql的实例

    try:
        mysql.info2_medicalDB()
        return "^_^The new user is registered successfully！\nusername："+newuser_info["username"]
    except pymysql.err.IntegrityError as e:
        print("FINALException Error is %s" % e)
        mysql.close_mysql()
        print("T.TRegistration failed...")
        return "T.TRegistration failed...\nThe username or name already exists!"
