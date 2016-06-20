from flask import Flask,render_template,redirect,request,flash
import time as dt
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
	var=dt.strftime('%l:%M:%S %p %b %d, %Y')
	return render_template('table2.html',var=var)  

if __name__ == '__main__':
	app.run('0.0.0.0',debug=True)
