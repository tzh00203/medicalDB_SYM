import pymysql


class login_medicaldb:  # 创建连接MYSQL的类
    def __init__(self, username, host, db, passwd, user_info):
        self.user_info = user_info
        self.username = username
        self.host = host
        self.db = db
        self.passwd = passwd
        self.conn = self.conn_mysql()
        # medicaldb中users表已有用户信息
        self.user_dict = {}
        # sql语句初始化
        self.sql = "SELECT username, password FROM users;"
        self.result = None

    def user_dict_update(self, result):             # medicaldb已有用户信息初始化
        for user in result:
            self.user_dict[user[0]] = user[1]

    def conn_mysql(self):  # 创建数据库连接
        conn = pymysql.connect(user=self.username, host=self.host, db=self.db, password=self.passwd, autocommit=True)
        print("----------Mysql is Opened----------")
        return conn

    def close_mysql(self):  # 关闭数据库, 有提示消息
        self.conn.close()
        print("----------Mysql is Closed----------")

    def info2_medicalDB(self):  # 与mysql进行交互,连接medicaldb数据库, 验证用户登录信息
        cur = self.conn.cursor()

        cur.execute(self.sql)
        result = cur.fetchall()
        self.user_dict_update(result)
        print(self.user_dict)
        if self.user_info["username"] not in self.user_dict:
            self.result = "failure"
            return
        if self.user_dict[self.user_info["username"]] != self.user_info["password"]:
            self.result = "failure"
            return
        self.result = "success"


def user_2MDS(user_info):
    mysql = login_medicaldb('root', '127.0.0.1', 'medicaldb', 'tzh2002315', user_info)  # 创建login_medicaldb的实例

    try:
        mysql.info2_medicalDB()
        mysql.conn.cursor().close()
        mysql.close_mysql()
        return mysql.result
    except pymysql.err.IntegrityError as e:
        print("FINALException Error is %s" % e)
        mysql.close_mysql()
        print("T.TLogin failed...")
        return 'failure'
