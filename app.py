import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# Configurations 
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Set up an instance of PyMongo
mongo = PyMongo(app)


@app.route("/")
@app.route("/home")
def home():    
    return render_template("index.html")


@app.route("/get_terms")
def get_terms():
    terms = list(mongo.db.terms.find())
    return render_template("terms.html", terms=terms)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method =="POST":
        # check if user already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
            #"confirm_password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)
    
        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful")
        return redirect(url_for("account", username=session["user"]))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):

                # Log the user in
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "account", username=session["user"]))

            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("account.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")

    return redirect(url_for("login"))


@app.route("/add_term", methods=["GET", "POST"])
def add_term():
    if request.method == "POST":
        term = {
            "term_name": request.form.get("term_name"),
            "term_description": request.form.get("term_description"),
            "added_by": session["user"]
        }
        mongo.db.terms.insert_one(term)
        flash("Your entry successfully added!")
        return redirect(url_for("get_terms"))

    return render_template("add_term.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
