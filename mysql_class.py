import mysql.connector
import os
 
class Connect(object):

    def __init__(self, table_name):
        self.host = os.getenv("host")
        self.user = os.getenv("username")
        self.passwd = os.getenv("password")
        self.database = os.getenv("database")

        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd,
            database=self.database
            )
        self.mycursor = self.mydb.cursor()
        self.table_name = table_name

    def insert_into_table(self, data_dic):
        quantity = ''
        col_name = ''
        
        for count, key in enumerate(data_dic.keys()):
            col_name += ','+str(key)
            quantity += ','+'%s'

        col_name = col_name[1:]
        quantity = quantity[1:]
        
        sql = "INSERT INTO {} ({}) VALUES ({})".format(self.table_name, col_name, quantity)#sql語法

        for i in range(count+1):
            col_value = []

            for key in data_dic.keys():
                col_value.append(data_dic[key][i])

            self.mycursor.execute(sql,col_value)#sql python語法
        
        self.mydb.commit()#更新
        print("Inserted completely")
    
    def create_table(self, col_name_list):
        self.mycursor.execute("CREATE TABLE {} (name VARCHAR(255), url VARCHAR(255), no VARCHAR(255))".format(self.table_name))

    # def create_db(self, db_name):
    #     self.mycursor.execute("CREATE DATABASE {}".format(db_name))

#=========================以下為測試碼============================

# if __name__ == "__main__":
#     dic = {'name' : ['Github','Google'],'url' : ['https://www.github.com','https://www.google.com']}
#     job = Connect('test') 設置欲使用的table
#     job.insert_into_table(dic) 字典存入table
    
    
