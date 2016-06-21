import sqlite3

class database():
	
	def create_table(self):
		con=sqlite3.connect('database.db')
		con.execute("CREATE TABLE Table1\
			(s_no INTEGER PRIMARY KEY AUTOINCREMENT,\
			date TEXT,\
			value INT);")
		con.close()

	def insert(self,date,value):
		con=sqlite3.connect('database.db')
		con.execute("INSERT INTO Table1(date,value)\
		VALUES(?,?);",(date,value))
		con.commit()
		con.close()
	def get(self):
		con=sqlite3.connect('database.db')
		cur=con.execute("SELECT * FROM Table1 ORDER BY date DESC LIMIT 1")
		for data in cur:
			date=data[1]
			value=data[2]
			return date,value
		con.close()

db=database()