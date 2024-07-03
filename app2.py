from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Recipe, MealPlan, Favorite
import requests
'''
flask app page for our recipe finder project
'''

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

SPOONACULAR_API_BASE_URL = "https://api.spoonacular.com/recipes"
SPOONACULAR_API_KEY = app.config['SPOONACULAR_API_KEY']

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    '''Returns a list of recipes based on provided ingredients.
    '''
    query = request.args.get('query', 'pasta')
    response = requests.get(f"{SPOONACULAR_API_BASE_URL}/search", params={
        'query': query,
        'apiKey': SPOONACULAR_API_KEY
    })
    if response.status_code == 200:
        return jsonify(response.json()), 200
    return jsonify({'error': 'Failed to fetch recipes'}), 500

@app.route('/api/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
    '''Returns details of a specific recipe by its ID.
    '''
    response = requests.get(f"{SPOONACULAR_API_BASE_URL}/{id}/information", params={
        'apiKey': SPOONACULAR_API_KEY
    })
    if response.status_code == 200:
        return jsonify(response.json()), 200
    return jsonify({'error': 'Failed to fetch recipe'}), 500

@app.route('/api/mealplan', methods=['GET', 'POST'])
def meal_plan():
    '''Creates a meal plan based on user preferences.
    '''
    if request.method == 'POST':
        data = request.json
        new_meal = MealPlan(date=data['date'], recipe_id=data['recipe_id'])
        db.session.add(new_meal)
        db.session.commit()
        return jsonify({'message': 'Meal plan created'}), 201
    
    meal_plans = MealPlan.query.all()
    return jsonify([{
        'id': meal_plan.id,
        'date': meal_plan.date,
        'recipe_id': meal_plan.recipe_id
    } for meal_plan in meal_plans]), 200

@app.route('/api/favorites', methods=['GET', 'POST'])
def favorites():
    '''GET: Returns the user's favorite recipes.
    POST: Adds a recipe to the user's favorites.
    '''
    if request.method == 'POST':
        data = request.json
        new_favorite = Favorite(user_id=data['user_id'], recipe_id=data['recipe_id'])
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify({'message': 'Favorite added'}), 201
    
    user_id = request.args.get('user_id')
    favorites = Favorite.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': favorite.id,
        'user_id': favorite.user_id,
        'recipe_id': favorite.recipe_id
    } for favorite in favorites]), 200

if __name__ == '__main__':
    app.run(debug=True)
