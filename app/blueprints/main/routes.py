from flask import render_template, current_app as app, request, redirect, url_for, flash
from datetime import datetime as dt
from app.blueprints import pokemon
from app.blueprints.pokemon.models import Pokemon, User
from app import db
from flask_login import current_user, login_required

from app.blueprints.pokemon.routes import pokemon_page


# MAIN APPLICATION ROUTES
@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    
   return render_template('main/home.html', pokemons=[post.to_dict() for post in Pokemon.query.filter_by(owner=current_user.get_id()).order_by(Pokemon.date_created.desc()).all()])
   

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    return render_template('main/profile.html', pokemons=[post.to_dict() for post in Pokemon.query.filter_by(owner=current_user.get_id()).order_by(Pokemon.date_created.desc()).all()])
