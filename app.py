# Import dependencies.
import os

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template

# basedir = os.path.abspath(os.path.dirname(__file__))

#################################################
# Database Setup
#################################################
protocol = 'postgresql'
username = 'postgres'
password = 'postgres'
host = 'localhost'
port = 5432
database_name = 'project03-group11_db'
rds_connection_string = f'{protocol}://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(rds_connection_string)

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Movie = Base.classes.movie
Actor = Base.classes.actor
Director = Base.classes.director

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# API Routes
@app.route("/api/top10actors")
def top10actors():
   # Create our session (link) from Python to the database..
   session = Session(engine)

   # Return a list of top 10 actor names.
   results = session.query(Actor.name).limit(10).all()

   # Close session.
   session.close()

   return jsonify(results)

# @app.route("/api/v1.0/justice-league/real_name/<real_name>")
# def justice_league_by_real_name(real_name):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = real_name.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["real_name"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": f"Character with real_name {real_name} not found."}), 404

# @app.route("/api/v1.0/justice-league/superhero/<superhero>")
# def justice_league_by_superhero__name(superhero):
#     """Fetch the Justice League character whose superhero matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = superhero.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["superhero"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": "Character not found."}), 404

# Web Routes
@app.route("/")
def welcome():
   return render_template("/index.html")

# class Movie(db.Model):
#     cast_id = db.Column(db.Integer, primary_key=True)
#     character = db.Column(db.String(100), nullable=False)
#     department = db.Column(db.String(100), nullable=False)
#     gender = db.Column(db.String(80), unique=True, nullable=False)
#     age = db.Column(db.Integer)
#     created_at = db.Column(db.DateTime(timezone=True),
#                            server_default=func.now())
#     bio = db.Column(db.Text)

#     def __init__(self, name, city, addr,pin):
#         self.name = name
#         self.city = city
#         self.addr = addr
#         self.pin = pin

# def __repr__(self):
#    return f'<Movie {self.firstname}>'

# Define main behavior.
if __name__ == "__main__":
   # db.create_all()
   app.run(debug=True)