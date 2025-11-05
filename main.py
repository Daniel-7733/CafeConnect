from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import path, makedirs


"""
Cafés should have Wifi & Power 
(A Electrical outlet for laptop, 
phone, or anything that charge with power)
"""



db: SQLAlchemy = SQLAlchemy()
app: Flask = Flask(__name__)


app.config["SECRET_KEY"] = "dev-secret"

makedirs(app.instance_path, exist_ok=True)
db_path: str = path.join(app.instance_path, "book.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
with app.app_context():
    db.create_all()


class Cafe(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    location: str = db.Column(db.String(100), nullable=False)
    wifi: str = db.Column(db.String(100), nullable=False)
    power: str = db.Column(db.String(100), nullable=False)
    link: str = db.Column(db.String(500), nullable=False)


cafe: list[dict[str, str]] = [
    {"Name": "Brewed Awakening", "Location": "E 1st Ave", "Wifi": "📶", "Power": "🔌", "Link": "https://www.brewedawakening.com/"},
    {"Name": "cafe Medina", "Location": "Clark Dr", "Wifi": "📶", "Power": "🔌", "Link": "https://www.medinacafe.com/"}
    ]

# cafe_titles: set[str] = set([key for element in cafe for key, value in element.items()])


@app.route("/")
def index() -> str:
    return render_template("index.html", cafe_list=cafe)

# Todo: Add function to store new good Cafés or Cafés
# Todo: Get information from the database
# Todo: (Maybe) getting more dynamic program that get all good Cafés base on user ip address.

if __name__ == "__main__":
    app.run(debug=True)
