import sqlite3

 

sqlCon = sqlite3.connect("DB이름")

sqlCur = sqlCon.cursor()

sqlCur.execute("SELECT * FROM 테이블이름")

 

print("열이름1 열이름2")

print("---------------------")

 

while (True) :

    sqlRow = sqlCur.fetchone()

    if sqlRow == None :

        break;

    data1 = sqlRow[0]

    data2 = sqlRow[1]

    print("%s %d" % (data1, data2))

 

    sqlCon.close()
