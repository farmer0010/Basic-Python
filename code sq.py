import sqlite3

mycon = sqlite3.connect("DB이름")

mycur = mycon.cursor()

 

while (True) :

    data1 = input("열 데이터1 ==> ")

    if data1 == "" :

        break;

    data2 = input("열 데이터2 ==> ")

    mystr = "INSERT INTO 테이블이름 VALUES("+data1+","+data2+")"

    mycur.execute(mystr)

 

mycon.commit()

mycon.close() 
