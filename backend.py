import mysql.connector
import mysql
## Creating a database
"""my_db = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd= "PASS"
    )

my_cursor = my_db.cursor()
my_cursor.execute("CREATE DATABASE routine")"""

def connect():
    my_db = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd= "PASS",
        database= "routine"
        )
    
    my_cursor = my_db.cursor()
    my_cursor.execute("CREATE TABLE IF NOT EXISTS routine (ID INT PRIMARY KEY , Date DATE , Earnings VARCHAR(255) , Exercise VARCHAR(255) , Studying VARCHAR(255) , Reading VARCHAR(255) ,Programming VARCHAR(255))")
    my_db.commit()
    my_db.close()
 
def insert(date , Programming,read, exercise , study ,earnings  ):
    my_db = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd= "PASS",
        database= "routine"
        )
    
    my_cursor = my_db.cursor()
    sql = """INSERT INTO routine VALUES (NULL, "%s","%s","%s","%s","%s","%s")"""
    vals =(date , int(earnings) , exercise , study , read , Programming)
    my_cursor.execute(sql,vals)
    my_db.commit()
    my_db.close()
    
def view():
    my_db = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd= "PASS",
        database= "routine"
        )
    
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM routine")
    rows = my_cursor.fetchall()
    my_db.commit()
    my_db.close()
    return rows

def delete(id):
    my_db = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd= "PASS",
        database= "routine"
        )
    
    my_cursor = my_db.cursor()
    my_cursor.execute("DELETE FROM routine WHERE id=? ", (id,))
    my_db.commit()
    my_db.close()

def search(date="" , Programming="",read="", exercise="" , study="" ,earnings=""):
    my_db = mysql.connector.connect(
        host= "localhost",
        user = "root",
        passwd= "PASS",
        database= "routine"
        )
    
    my_cursor = my_db.cursor()
    my_cursor.execute("SELECT * FROM routine WHERE date=? OR earnings=? OR exercise=? OR study=? OR read=? OR python=?" , date , earnings , exercise , study , read , Programming)
    rows = my_cursor.fetchall()
    my_db.commit()
    my_db.close()
    return rows   

connect()    