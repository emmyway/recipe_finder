from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("0-cover.html")

@app.route("/api/recipes")
def recipes():
    '''Returns a list of recipes based on provided ingredients.
    '''
    return render_template("0-cover.html")

@app.route("/api/recipe/{id}")
def recipe_detail(int:id):
    '''Returns details of a specific recipe by its ID.
    '''
    return render_template
