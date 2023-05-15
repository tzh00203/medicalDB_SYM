import pymysql
import time


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


class function2mysql:  # 创建连接MYSQL的类
    def __init__(self, username, host, passwd, database):

        self.username = username
        self.host = host
        self.passwd = passwd
        self.database = database
        self.conn = self.conn_mysql()
        # sql语句初始化
        self.sql = None

    def conn_mysql(self):   # 创建数据库连接
        try:
            conn = pymysql.connect(user=self.username, host=self.host, password=self.passwd, db=self.database)
            print("-------与medicaldb数据库连接成功-------")
            return conn
        except pymysql.err.Error as err:
            print("Exception Error is %s" % err)
            print("-------与medicaldb数据库连接失败-------")

    def close_mysql(self):  # 关闭数据库, 有提示消息
        self.conn.close()
        print("-------与medicaldb数据库连接断开-------")

    def data_mysql(self, table_name):   # 与mysql进行交互

        cur = self.conn.cursor()
        sql = "SELECT * FROM " + table_name + ";"
        cur.execute(sql)
        result = cur.fetchall()
        for value in result:
            print(value)
        print(table_name+"表格数据更新完成...")
        return result

    def and_mysql(self, table1, table2, dep_name):

        final_result = []
        cur = self.conn.cursor()
        # 条件查询，看一下该科室有哪些医生

        sql = "SELECT doc_name,level,join_date FROM " + \
              table1 + " WHERE dep_name = '" + dep_name + "';"
        print(sql)
        cur.execute(sql)
        result1 = list(cur.fetchall())
        print(result1)
        doc_num = len(result1)
        for i in range(doc_num):
            final_result.append(list(result1[i]))
            sql = "SELECT * FROM " + \
                  table2 + " WHERE doc_name = '" + final_result[i][0] + "';"
            print(sql)
            cur.execute(sql)
            final_result[i].extend(list(cur.fetchall()[0])[1:])
        # 此时得到的二维结果列表没有调整到我们想要的属性顺序
        print(final_result)
        # 调整顺序
        final_result_new = []
        for i in range(doc_num):
            tmp_list = final_result[i][0:1]
            tmp_list.extend(final_result[i][3:6])
            tmp_list.extend(final_result[i][1:3])
            tmp_list.append(final_result[i][-1])
            final_result_new.append(tmp_list)
            # print(tmp_list)
        # 最终调整好属性顺序的结果列表
        print(final_result_new)
        return final_result_new, doc_num

    def pt_records_mysql(self, table, pt_name):

        cur = self.conn.cursor()

        # 没有这个病历本的情况
        sql = "select pt_name from " + table + ";"
        cur.execute(sql)
        result1 = cur.fetchall()
        pt_dict = {}
        for i in result1:
            pt_dict[list(i)[0]] = "yes"
        print(pt_dict)
        if pt_name not in pt_dict:
            return None, 0, 0
        # 条件查询，看一下有哪些患者
        sql = "SELECT pt_name, med_id,dis_date,dis_type,doc_name FROM " + \
              table + " WHERE pt_name = '" + pt_name + "';"
        print(sql)
        cur.execute(sql)
        result1 = cur.fetchall()
        print(result1)
        rows = len(result1)
        cols = len(result1[0])

        return result1, rows, cols

    # 注册新的科室
    def newdep_info2medicaldb(self, newdep_info):
        newdep_info_intro = None
        cur = self.conn.cursor()
        for i in range(len(newdep_info["introduction"])):
            if newdep_info["introduction"][i] == "后":
                newdep_info_intro = newdep_info["introduction"][i+2:].replace('\\', '/')
                break

        self.sql = "INSERT INTO departments(dep_name,  location, " + \
                   "introduction) Values("
        self.sql += "'{}', '{}', '{}'); "\
                    .format(newdep_info["dep_name"], newdep_info["location"],
                            newdep_info_intro)
        print(self.sql)
        try:
            cur.execute("use medicaldb;")
            cur.execute(self.sql)
            result = cur.fetchall()
            print(result)
            cur.execute("COMMIT;")
            return "^_^ DEP REGISTERED SUCCESSFULLY ！"
        except pymysql.err.Error as error_dep:
            print("error_dep Error is %s" % error_dep)
            print("T.TRegistration failed...")
            return "T.TRegistration failed...Existed DEP_NAME~"

    # 注册新的医生
    def newdoc_info2medicaldb(self, newdoc_info):
        newdoc_info_intro = None
        cur = self.conn.cursor()
        for i in range(len(newdoc_info["introduction"])):
            if newdoc_info["introduction"][i] == "后":
                newdoc_info_intro = newdoc_info["introduction"][i+2:].replace('\\', '/')
                break

        self.sql = "INSERT INTO doctors(doc_name,  age, " + \
                   "tel, gender, introduction) Values("
        self.sql += "'{}', '{}', '{}', '{}', '{}'); "\
                    .format(newdoc_info["doc_name"], newdoc_info["age"],
                            newdoc_info["tel"], newdoc_info["gender"],
                            newdoc_info_intro)
        print(self.sql)
        try:
            cur.execute("use medicaldb;")
            cur.execute(self.sql)
            result = cur.fetchall()
            print(result)
            cur.execute("COMMIT;")
            self.sql = "INSERT INTO departments_consist(dep_name,  doc_name, " + \
                       "level, join_date) Values("
            self.sql += "'{}', '{}', '{}', '{}'); "\
                        .format(newdoc_info["dep_name"], newdoc_info["doc_name"],
                                newdoc_info["level"], time.strftime('%Y.%m.%d')
                                )
            print(self.sql)
            cur.execute("use medicaldb;")
            cur.execute(self.sql)
            result = cur.fetchall()
            print(result)
            cur.execute("COMMIT;")
            return "^_^ DOC REGISTERED SUCCESSFULLY ！"

        except pymysql.err.Error as error_dep:
            print("error_dep Error is %s" % error_dep)
            print("T.TRegistration failed...")
            return "T.TRegistration failed...Existed DOC_NAME~"

    # 注册新的患者
    def newpt_info2medicaldb(self, newpt_info):

        cur = self.conn.cursor()

        self.sql = "INSERT INTO patients(pt_name,  age, gender, tel, " + \
                   "address, creation_date) Values("
        self.sql += "'{}', '{}', '{}', '{}', '{}', '{}'); "\
                    .format(newpt_info["pt_name"], newpt_info["age"], newpt_info["gender"],
                            newpt_info["tel"], newpt_info["address"], time.strftime('%Y.%m.%d')
                            )
        print(self.sql)
        try:
            cur.execute("use medicaldb;")
            cur.execute(self.sql)
            result = cur.fetchall()
            print(result)
            cur.execute("COMMIT;")
            return "^_^ PT REGISTERED SUCCESSFULLY ！"
        except pymysql.err.Error as error_dep:
            print("error_dep Error is %s" % error_dep)
            print("T.TRegistration failed...")
            return "T.TRegistration failed...Existed PT_NAME~"

    # 删除选中数据
    def delete_data(self, table_name, data_name, data_name_con):
        cur = self.conn.cursor()
        self.sql = "DELETE FROM " + table_name + " where " +\
                   data_name + " = '" + data_name_con + "';"
        print(self.sql)
        try:
            cur.execute("use medicaldb;")
            cur.execute(self.sql)
            result = cur.fetchall()
            print(result)
            cur.execute("COMMIT;")

        except pymysql.err.Error as delete_err:
            print("DELETE_Error is %s" % delete_err)
            print("T.T_DELETE failed...")

    # 搜索数据库中符合条件数据
    def search_mysql(self, key):   # 与mysql进行交互
        result_dict = {}
        cur = self.conn.cursor()
        table_names = ["departments", "doctors", "departments_consist", "patients"]
        for table_name in table_names:
            sql = "SELECT * FROM " + table_name + ";"
            cur.execute(sql)
            result = cur.fetchall()
            for value in result:
                if key in value:
                    print(value)
                    sql = "desc " + table_name + ";"
                    cur.execute(sql)
                    print(cur.fetchall())
                    result_dict[table_name] = value
        print(result_dict)
        if len(result_dict) != 0:
            return result_dict
        else:
            return "The desired associated data was not found in medicaldbT.T"


if __name__ == "__main__":

    print('用户名:root')
    print('主机名:127.0.0.1')
    print('数据库:medicaldb')
    try:    # 使用try--except
        mysql = function2mysql('root', '127.0.0.1', "tzh2002315", "medicaldb")
        mysql.conn_mysql()
        mysql.search_mysql("小丑")

    except pymysql.err.Error as e:
        print("Exception Error is %s" % e)
        print("-------与medicaldb数据库连接失败-------")
