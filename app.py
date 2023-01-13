import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

postgresql://username:password@host:port/database_name

app = Flask(__name__)

@app.route("/")
def welcome():
    return(
    f" Welcome to the Movie Dive API!<br/>"
    f"Available Routes:<br/>"
    f" /api/v1.0/Actors<br/>"
    f"/api/v1.0/Directors <br/>"
    f"/api/v1.0/Movies list<br/>"
   )

class Movie(db.Model):
    cast_id = db.Column(db.Integer, primary_key=True)
    character = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def show_all():
   return render_template('show_all.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
        flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)

def __repr__(self):
        return f'<Movie {self.firstname}>'


