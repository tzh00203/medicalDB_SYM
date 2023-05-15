import pymysql
import xlrd


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


def dataExcel_sqlFile(filename):

    mysql_table = filename.split('.')[0]  # 获取数据库是哪个表要新增数据
    output_sqlFile_name = "sqlFile_" + mysql_table + ".sql"
    output_sqlFile = open(output_sqlFile_name, "w+", encoding='utf-8')  # 表对应的数据插入sql文件
    output_sqlFile.write("use medicaldb;\n")

    excelFile = xlrd.open_workbook(filename)
    table = excelFile.sheet_by_name('Sheet1')
    rows = table.nrows   # 获取总行数
    sql = "INSERT INTO " + mysql_table + "("
    for col_name in table.row_values(0):
        if col_name != table.row_values(0)[-1]:
            sql += col_name + ', '
        else:
            sql += col_name + ' '
    sql += ') Values('
    for row in range(1, rows):
        sql_tmp = sql + str(table.row_values(row))[1:-1] + ");"
        output_sqlFile.write(sql_tmp + '\n')
    output_sqlFile.write("COMMIT;")  # INSERT DELETE UPDATE语句需要提交更新数据库
    output_sqlFile.close()
    return output_sqlFile_name


class py2mysql:  # 创建连接MYSQL的类
    def __init__(self, username, host, passwd, database, sql_name):
        self.file_name = sql_name
        self.username = username
        self.host = host
        self.passwd = passwd
        self.database = database
        self.conn = self.conn_mysql()

    def conn_mysql(self):   # 创建数据库连接
        conn = pymysql.connect(user=self.username, host=self.host, password=self.passwd, db=self.database)
        return conn

    def close_mysql(self):  # 关闭数据库, 有提示消息
        self.conn.close()
        print("----------Mysql is Closed----------")

    def modify_mysql(self):     # 向数据库添加表格、数据
        cur = self.conn.cursor()
        file_sql = open(self.file_name, encoding='utf8')  # 读取sql文件，并将结果返回到终端
        for sql in deal_sql(file_sql):
            try:
                print(sql)
                cur.execute(sql)
                result = cur.fetchall()
                print(result)
            # 如果mysql出现错误会报错, 然后继续执行下一条语句
            except pymysql.err.ProgrammingError as end:
                print("Exception Error is %s" % end)
            except pymysql.err.OperationalError as end:
                print("Exception Error is %s" % end)
        cur.execute("select * from doctors;")
        result = cur.fetchall()
        print(result)
        print(self.file_name + "文件数据插入成功！")
        cur.close()
        self.close_mysql()

    def inter_mysql(self):   # 与mysql进行交互
        cur = self.conn.cursor()

        while True:
            sql = input('输入SQL语句: ')
            cur.execute(sql)
            result = cur.fetchall()
            for i in result:
                print(str(i))
            end = input('按N断开连接，任意键继续... ')
            if end == 'N':
                break
        cur.close()
        self.close_mysql()


if __name__ == "__main__":

    sqlFile_name = dataExcel_sqlFile("patients_med_disease.xlsx")
    print('用户名:root')
    print('主机名:127.0.0.1')
    print('数据库:medicaldb')
    try:    # 使用try--except
        mysql = py2mysql('root', '127.0.0.1', "tzh2002315", "medicaldb", sqlFile_name)
        mysql.conn_mysql()
        mysql.modify_mysql()
        # mysql.inter_mysql()
    except pymysql.err.Error as e:
        print("OUTSIDE_Exception Error is %s" % e)
