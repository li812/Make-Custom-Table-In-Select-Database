import mysql.connector
#dbhost = input("Enter host name : ")
#dbuser = input("Enter username : ")
#dbpass = input("Enter password : ")
#Uncomment these lines if you want to configur connection profiles
mydbx =mysql.connector.connect(
    #host = dbhost,
    #user = dbuser,
    #password = dbpass
    host = "localhost",
    user = "root",
    password = ""
)
exex=mydbx.cursor()
exex.execute("Show Databases")
for i in exex:
    print(i)
dbname = input("Enter database name : ")
try:
    mydb = mysql.connector.connect(
        #host = dbhost,
        #user = dbuser,
        #password = dbpass,
        host = "localhost",
        user = "root",
        password = "",
        database = dbname
    )
    print("Trying to connect to database " + dbname)
    print("Connected successfully ;) ")

except mysql.connector.errors.ProgrammingError :
    print("Trying to connect to database " + dbname)
    print("Something went wrong!")
except NameError :
    print("Trying to connect to database " + dbname)
    print("Something went wrong!")

try:
    exe=mydb.cursor()
    exe.execute("SHOW TABLES")
    print("The database ",dbname," currently has these tables : ")
    for i in exe:
        print(i)
    ctb = "CREATE TABLE "
    tname =input("Enter table name : ")
    tval = input("Enter table values inside ( ) with datatype seperated by , : ")
    sql = str(ctb+tname+tval)
    exe.execute(sql)
    mydb.commit()
    print("Trying to create table " + tname)
    print("Table successfully Created ;) ")
except mysql.connector.errors.ProgrammingError:
    print("Trying to create table " + tname)
    print("Something went wrong!")
