import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS students")

#Create users table  in db_web database
sql ='''CREATE TABLE "students" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"NAME"	TEXT,
	"SURNAME"	TEXT,
    "DATE_OF_BIRTH" TEXT,
    "CLASS" TEXT,
    "ADDRESS" TEXT,
    "GENDER" TEXT,
    "ACTIVE" TEXT DEFAULT yes
)'''
cur.execute(sql)

sql ='''CREATE TABLE "admins" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"NAME"	TEXT,
    "LOGIN" TEXT,
    "PASSWORD" TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()