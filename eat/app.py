from flask import Flask ,render_template , request

app=Flask(__name__)
# userdb= dataset.connect("sqlite:///data.db")
# usertable = db('user')
@app.route("/")
def home():
	return render_template('home.html')
@app.route("/resturants")

def resturants():
	return render_template('resturants.html')

@app.route("/tmenu")
def tmenu():
	return render_template('tmenu.html')
@app.route("/mmenu")
def mmenu():
	return render_template('mmenu.html')
@app.route("/thilandy")
def thilandy():
	return render_template('thilandy.html')
@app.route("/submax")
def submax():
	return render_template('submax.html')
@app.route("/info")
def info():
	return render_template('info.html')
@app.route("/why")
def why():
	return render_template('why.html')
@app.route("/about")
def about():
	return render_template('about.html')
@app.route("/submit" , methods =['POST'])
def submit():
	user = request.form['Name']
	return render_template('submit.html', username=user)
if __name__ == '__main__':
	app.run(port=8000,debug=True)