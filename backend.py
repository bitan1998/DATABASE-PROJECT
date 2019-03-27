import sqlite3

def studentData():
	conn=sqlite3.connect("student.db")
	conn.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY,StdID text,Firstname text,Surname text, \
	              Dob text, Emailid text ,Subject text,Address text,Mobile text,RfId INTEGER)")
	conn.commit()
	conn.close()

def addStdRec(StdId,Firstname,Surname,Dob,Emailid,Subject,Address,Mobile,RfId):
	conn=sqlite3.connect("student.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,?,?)",(StdId,Firstname,Surname,Dob,Emailid,Subject,Address,Mobile,RfId))
	conn.commit()
	conn.close()

def viewData():
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM student")
	rows=cur.fetchall()
	conn.close()
	return rows

def deleteRec(id):
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("DELETE FROM student WHERE id=?",(id,))
	conn.commit()
	conn.close()

def searchData(StdId):
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM student WHERE StdId=?",(StdId,))
	rows=cur.fetchall()
	conn.close()
	return rows
	
def searchAllData():
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("SELECT * FROM student")
	rows=cur.fetchall()
	conn.close()
	return rows

def dataUpdate(StdId,Firstname="",Surname="",Dob="",Emailid="",Subject="",Address="",Mobile="",RfId=""):
	conn=sqlite3.connect("student.db")
	cur=conn.cursor()
	cur.execute("UPDATE student SET Firstname=? , Surname=? , Dob=? , Emailid=? , Subject=? , Address=? , Mobile=? , RfId=? where id=?",\
				 (Firstname,Surname,Dob,Emailid,Subject,Address,Mobile,RfId,StdId,))
	conn.commit()
	conn.close()


