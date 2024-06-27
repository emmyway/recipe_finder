from flask import Flask, render_template
'''
flask app page for our recipe finder project
'''

app = Flask(__name__)

@app.route("/")
def cover():
    return render_template("template/0-cover.html")

@app.route("/home")
def home():
    return render_template("template/1-home.html")

@app.route("/api/recipes")
def recipes():
    '''Returns a list of recipes based on provided ingredients.
    '''
    return render_template("template/2-find_recipes.html")

@app.route("/api/recipe/{id}")
def recipe_detail(int:id):
    '''Returns details of a specific recipe by its ID.
    '''
    return render_template("template/4-recipe_detail.html")

@pp.route("/api/mealplan", method['POST'])
def meal_plan():
    '''Creates a meal plan based on user preferences.
    '''
    return render_template(url_for('template', filename='4-recipe_detail.html'))

@app.route("/api/favorites", method['GET', 'POST', 'DELETE'])
def favorites():
    '''GET: Returns the user's favorite recipes.
    POST: Adds a recipe to the user's favorites.
    DELETE: Removes a recipe from the user's favorites.
    '''
    return render_template(url_for("template", filename='4-recipe_detail.html'))


if __name__ = "__main__":
    app.run(debug=True)
