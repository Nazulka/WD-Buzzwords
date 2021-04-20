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

# Home Page 
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")


# Returns all terms from db
@app.route("/get_terms")
def get_terms():
    # Sorts results alphabetically
    terms = list(mongo.db.terms.find().sort('term_name', 1))
    return render_template("glossary.html", terms=terms)


# Filter results by first letter
# @app.route("/filter_terms/first_letter")
# def filter_terms(first_letter):
#     filter = list(mongo.db.terms.find({'term_name': {'$regex': 'index[0]'}}))
#     print("hello")
#     return render_template("glossary.html", first_letter=filter)


# Filter results by first letter
@app.route("/filter_terms")
def filter_terms(letter):
    result = {}
    for term in result:
        if letter in result:
            result[letter].append(term)
        else:
            result[letter] = [term]
            print("hello")
    return render_template("glossary.html", result=result)


# Returns search results
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    terms = list(mongo.db.terms.find({"$text": {"$search": query}}))
    # Displays results on Glossary Page
    return render_template("glossary.html", terms=terms)


# Sign up function
@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        # check if user already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        # check if password and confirm_password inputs match
        confirm_password = request.form.get("confirm_password")
        password = request.form.get("password")

        if password != confirm_password:
            flash("Passwords don't match!")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        # put the new user into "session" cookie
        session["user"] = request.form.get("username").lower()

        flash("Registration Successful")
        return redirect(url_for("account", username=session["user"]))
    return render_template("sign_up.html")


# Log in function
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
                flash("Welcome back, {}".format(
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


# Returns User Profile page
@app.route("/account/<username>", methods=["GET", "POST"])
def account(username):
    # grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Get the session user's added entries from the db sorted alphabetically
    terms = list(mongo.db.terms.find().sort('term_name', 1))

    if session["user"]:
        return render_template("account.html", username=username, terms=terms)

    return redirect(url_for("login"))


# Log out function
@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")

    # return to Log in Page
    return redirect(url_for("login"))


# Adds new terms
@app.route("/add_term")
def add_term():
    return render_template("add_term.html", terms=mongo.db.terms.find())


# Inserts new unique terms into the db
# Credit to Tutor Support for providing a template for this function
@app.route("/insert_term", methods=['POST'])
def insert_term():
    new_term = request.form.get("term_name")
    terms = mongo.db.terms
    existing_term = terms.count_documents({
        'term_name': new_term.upper()}, limit=1)

    # Add unique term into the database
    if existing_term == 0:
        terms.insert_one(
        {
            "term_name": request.form.get("term_name").upper(),
            "term_description": request.form.get("term_description"),
            "added_by": session["user"]
        })
        flash("Your entry successfully added!")
        return redirect(url_for("account", username=session["user"]))

    else:
        # Display flash message if already in the db
        flash("This term already exists in the dictionary!")
    return render_template("add_term.html")


# Edits terms if added_by the user
@app.route("/edit_term/<term_id>", methods=["GET", "POST"])
def edit_term(term_id):
    if request.method == "POST":
        submit = {
            "term_name": request.form.get("term_name"),
            "term_description": request.form.get("term_description"),
            "added_by": session["user"]
        }
        # Update the db
        mongo.db.terms.update({"_id": ObjectId(term_id)}, submit)
        flash("Entry successfully updated!")

    term = mongo.db.terms.find_one({"_id": ObjectId(term_id)})
    return render_template("edit_term.html", term=term)


# Removes term from the db if added_by user
@app.route("/delete_term/<term_id>")
def delete_term(term_id):
    mongo.db.terms.remove({"_id": ObjectId(term_id)})
    flash("Entry Successfully Deleted")
    # Returns to the Profile Page
    return redirect(url_for("account", username=session["user"]))


# A handler for '404 Page not found' exception
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


# A handler for '500 Internal server error'
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error), 500


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
