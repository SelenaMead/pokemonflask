from app import create_app, db


app = create_app()
from app.blueprints.pokemon.models import User, Pokemon
@app.shell_context_processor
def make_context():
    return {
        'db': db,
        'User': User,
        'Pokemon': Pokemon
    }