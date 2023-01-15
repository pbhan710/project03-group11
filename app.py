# Import dependencies.
import os
from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

postgresql://username:password@host:port/database_name

#################################################
# Flask Routes
#################################################

# API Routes
@app.route("/api/top10actors")
def justice_league():

   result = ''
   return jsonify(result)


@app.route("/api/v1.0/justice-league/real_name/<real_name>")
def justice_league_by_real_name(real_name):
    """Fetch the Justice League character whose real_name matches
       the path variable supplied by the user, or a 404 if not."""

    canonicalized = real_name.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["real_name"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404


@app.route("/api/v1.0/justice-league/superhero/<superhero>")
def justice_league_by_superhero__name(superhero):
    """Fetch the Justice League character whose superhero matches
       the path variable supplied by the user, or a 404 if not."""

    canonicalized = superhero.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["superhero"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": "Character not found."}), 404

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