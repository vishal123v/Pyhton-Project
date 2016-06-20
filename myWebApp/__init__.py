from flask import Flask
from flask import render_template
from flask import request, redirect

app = Flask(__name__)
app.secret_key = 'my secret key is this'
userName = 0
@app.route('/', methods=['GET','POST'])
def home():
	global userName
	if request.method == 'POST':
		userName = request.form['num1']
		pwd = request.form['pwd']
		print '\n\t',userName, pwd,'\n\t'
		if userName == 'admin' and pwd == 'admin':
			return redirect('/index')
	return render_template('home.html', var = 'abc')

@app.route('/index', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		userName = request.form['num1']
		pwd = request.form['pwd']
		
	return render_template('index.html')

if __name__ == '__main__':
	app.run('0.0.0.0',debug=True)
