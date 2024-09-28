from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database with SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress warning    


# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a simple User model (table in SQLite)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

@app.route('/')
def home():
    return "Hello, Flask with SQLite!"

if __name__ == '__main__':
    # Create the database and tables within the app context
    with app.app_context():
        db.create_all()
    app.run(debug=True)
