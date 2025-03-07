from flask import Flask, request, redirect, url_for, render_template
from flask import session as login_session

app = Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"


##### Code here ######
@app.route("/")
def home():
	return render_template("home.html")


@app.route("/store")	
def store():
	return render_template("store.html")


@app.route("/cart")
def cart():

	return render_template("cart.html")	

@app.route("/about")
def about():
	return render_template("about.html")
#####################


if __name__ == '__main__':
    app.run(debug=True)