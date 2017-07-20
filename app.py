from flask import Flask, render_template , request
import random
app = Flask(__name__)


@app.route('/')
def index():
	quotes=["if you smart you will suceese","if you smile alot you will be rich","you should be optimistic"]
	names=["hade","khaled","bakiza","renan"]
	countries=["palestine","egypt","u.s","china"]
	return render_template("index.html" ,quotes=random.choice(quotes),names=random.choice(names),countries=random.choice(countries))
@app.route('/contact')
def con():
	return render_template("contact.html")
	
@app.route('/about')

def aboutme():
	return render_template("about.html")

@app.route("/hello" , methods=["post"])
def hello():
	user_firstname = request .form['firstname']
	user_lastname = request .form['lastname']
	user_messege = request .form['messege']
	user_gender = request .form['gender']
	#return user_firstname + " "+user_lastname + " "+user_gender+" "+user_messege
	return render_template("NAM.html" ,firstname = user_firstname , lastname = user_lastname , messege = user_messege)



if __name__=="__main__":
	app.run()