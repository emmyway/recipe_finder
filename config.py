mport os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql+mysqlconnector://username:password@localhost/recipe_finder_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY', 'your_spoonacular_api_key')
