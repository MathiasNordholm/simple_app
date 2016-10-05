from flask import Flask, render_template 
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def second():
	return render_template('new_web.html')

app.run(debug=True)