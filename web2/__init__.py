from flask import Flask,render_template,redirect,request,flash
import time as dt
from configsql import db

app=Flask(__name__)
app.secret_key='This is my page'

@app.route('/',methods=['GET','POST'])
def home():
	if request.method == 'POST':
		name=request.form['username']
		pwd=request.form['pwd']
		if name=='user' and pwd=='password':
			return redirect('/table') 
		else:
			#return "password wrong"
			flash("password wrong")
	return render_template('home2.html')

@app.route('/table')
def table():
	try:
		date,value =db.get()
	except Exception,e:
		date="table empty"
		value=-1
		print e 
	return render_template('table2.html',date=date,value=value)  

if __name__ == '__main__':
	try:
		db.create_table()
	except Exception, e:
		print e

	app.run('0.0.0.0',port=8000,debug=True)
	