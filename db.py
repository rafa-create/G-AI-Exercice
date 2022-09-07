import datetime 
import mysql.connector


def init_db(db_name): #Initiate DB when run main.py
    db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    passwd="", 
    database=db_name
) 
    #Create a database cursor to perform SQL operations
    cur = db.cursor()
    sql= "CREATE TABLE IF NOT EXISTS availibilities (S_time DATETIME(0), E_time DATETIME(0))"
    cur.execute(sql)
    sql= "CREATE TABLE IF NOT EXISTS reservations (title VARCHAR(255) ,email VARCHAR(255),S_time DATETIME(0), E_time DATETIME(0))"
    cur.execute(sql)
    cur.execute("TRUNCATE TABLE `reservations`")
    cur.execute("TRUNCATE TABLE `availibilities`")
    cur.execute("INSERT INTO availibilities (`S_time`,`E_time`) VALUES (%s,%s)",('2021-08-07 19:30:00','2050-09-08 00:00:00'))
    db.commit()
    db.close()
    return('ok')

def insert_db(title,email,S_time,E_time,db_name):#Add new reservations in DB
    db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    passwd="", 
    database=db_name
) 
    #Create a database cursor to perform SQL operations
    cur = db.cursor()
    cur.execute("INSERT INTO reservations (`title`, `email`,`S_time`,`E_time`) VALUES (%s,%s,%s,%s)",(title,email,S_time,E_time))
    db.commit()
    db.close()

def insert_av(L,db_name):#Add new availibilities in DB
    db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    passwd="", 
    database=db_name
) 
    #Create a database cursor to perform SQL operations
    cursor = db.cursor()
    cursor.execute("TRUNCATE TABLE `availibilities`")
    c=len(L)//2
    for i in range (c):
        cursor.execute("INSERT INTO availibilities (`S_time`,`E_time`) VALUES (%s,%s)",(L[i*2],L[i*2+1]))
    #Validate the transaction
    db.commit()
    db.close()

def printa(db_name,table):#Return the a html with of availabilities or meetings
    db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    passwd="", 
    database=db_name
) 
    html="<h1>My "+table+" : </h1><br>"
    cursor = db.cursor()
    query="select * from "+table
    cursor.execute(query)
    rows=cursor.fetchall()
    c=1
    for row in rows:
        html+="Line "+str(c)+":     " 
        c+=1
        for col in row:
            html+=str(col)+'   |   '
        html+="<br>"
    html+="<br>"
    cursor.close()
    return html

def ava(db_name):#Return the list of availabilities from the DB
    db = mysql.connector.connect( 
    host="localhost", 
    user="root", 
    passwd="", 
    database=db_name
) 
    A=[]
    cursor = db.cursor()
    query="select * from availibilities"
    cursor.execute(query)
    rows=cursor.fetchall()
    for row in rows:
        for col in row:
            A.append(col)
    cursor.close()
    return A