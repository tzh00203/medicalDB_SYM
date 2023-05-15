import pymysql


def deal_sql(fp):
    SQL = []
    sql_list = fp.read().split(';')[:-1]
    for x in sql_list:
        line = x.split('\n')
        L = ''
        for y in line:
            l = y.split('#', 1)[0].split('-- ', 1)[0]
            L = L + ' ' + l

        # sql语句添加分号结尾
        sql_item = L + ';'
        SQL.append(sql_item)
    return SQL


class creator_Mysql:  # 创建连接MYSQL的类
    def __init__(self, username, host, passwd):

        self.username = username
        self.host = host
        self.passwd = passwd
        self.conn = self.conn_mysql()

    def conn_mysql(self):  # 创建数据库连接
        conn = pymysql.connect(user=self.username, host=self.host, password=self.passwd)
        return conn

    def close_mysql(self):  # 关闭数据库, 有提示消息
        self.conn.close()
        print("----------Mysql is Closed----------")

    def init_medicalDB(self):  # 与mysql进行交互,创建medicaldb数据库
        cur = self.conn.cursor()
        file_sql = open("medical数据库新增表.sql", encoding='utf8')  # 读取medicaldb创建的sql文件，并将结果返回到终端
        for sql in deal_sql(file_sql):
            try:
                cur.execute(sql)
                result = cur.fetchall()
                if result != '()':
                    print(result)
            # 如果mysql出现错误会报错, 然后继续执行下一条语句
            except pymysql.err.ProgrammingError as end:
                print("Exception Error is %s" % end)
            except pymysql.err.OperationalError as end:
                print("Exception Error is %s" % end)

        cur.close()
        self.close_mysql()
        print("^_^医疗系统数据库创建成功！命名为：medicaldb")


if __name__ == "__main__":

    print('用户名:root')
    print('主机名:127.0.0.1')
    mysql = creator_Mysql('root', '127.0.0.1', 'tzh2002315')  # 创建creator_Mysql的实例
    mysql.conn_mysql()
    try:
        mysql.init_medicalDB()

    except pymysql.err.ProgrammingError as e:
        print("FINALException Error is %s" % e)
        mysql.close_mysql()
        print("T.T医疗系统数据库创建失败...")
    except pymysql.err.OperationalError as e:
        print("FINALException Error is %s" % e)
        mysql.close_mysql()
        print("T.T医疗系统数据库创建失败...")
