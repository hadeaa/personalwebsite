from flask import Flask, render_template
import random
app = Flask(__name__)


@app.route('/')
def index():
	quotes=["if you smart you will suceese","if you smile alot you will be rich","you should be optimistic"]
	names=["hade","khaled","bakiza","renan"]
	countries=["palestine","egypt","u.s","china"]
	return render_template("index.html" ,quotes=random.choice(quotes),names=random.choice(names),countries=random.choice(countries))

	
@app.route('/about')

def aboutme():
	return render_template("about.html")
if __name__=="__main__":
	app.run()