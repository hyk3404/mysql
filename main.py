import mysql_class
import os
import click
import mysql.connector

def main():
    host = "localhost"
    user = "newuser"
    passwd = "password"
    database = "spotify_db"

    mydb = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=database
            )

    mycursor = mydb.cursor()

    dic = {'name' : ['Github','Google'],'url' : ['https://www.github.com','https://www.google.com']}
    
    mysql_class.Connect.insert_into_table('test',dic)

main()