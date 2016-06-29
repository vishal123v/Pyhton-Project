import sqlite3

class database():
	
	def create_table(self):
		con=sqlite3.connect('database.db')
		con.execute("CREATE TABLE Table1\
			(s_no INTEGER PRIMARY KEY AUTOINCREMENT,\
			date TEXT,\
			temp INT);")
		con.close()

	def insert(self,date,temp):
		#print "insert function"
		con=sqlite3.connect('database.db')
		con.execute("INSERT INTO Table1(date,temp)\
		VALUES(?,?);",(date,temp))
		con.commit()
		con.close()
	def get(self):
		con=sqlite3.connect('database.db')
		cur=con.execute("SELECT * FROM table1 ORDER BY date DESC ")
		for data in cur:
			date=data[1]
			temp=data[2]
			return date,temp
		con.close()

db=database()