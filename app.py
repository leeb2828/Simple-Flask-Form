import routes
from flask import Flask
import os 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'A secret'

# Home page (where you will add a new user)
app.add_url_rule('/', view_func=routes.index)
# "Thank you for submitting your form" page
app.add_url_rule('/submitted', methods=['GET', 'POST'], view_func=routes.submitted)
# Viewing all the content in the database page
app.add_url_rule('/database', view_func=routes.view_database)
app.add_url_rule('/modify<the_id>/<modified_category>', methods=['GET', 'POST'], view_func=routes.modify_database)
app.add_url_rule('/delete<the_id>', methods=['GET', 'POST'], view_func=routes.delete)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # no warning messages
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db' # for using the sqlite database
db = SQLAlchemy(app)
# Create User Table
class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50))
    job = db.Column(db.String(50))

def insert_data(**kwargs):
    db.session.add(User(**kwargs))
    db.session.commit()

def modify_data(the_id, col_name, user_input):
    user = User.query.filter_by(id=the_id).first()
    setattr(user, col_name, user_input)
    db.session.commit() 

def delete_data(the_id):
    the_user = User.query.filter_by(id=the_id).first()
    db.session.delete(the_user)
    db.session.commit()

def get_all_rows_from_table():
    users = User.query.all()
    return users 
    
db_is_new = db.create_all() if not os.path.exists('info.db') else None
if __name__ == '__main__':
    app.run(host=5000,debug=True)
