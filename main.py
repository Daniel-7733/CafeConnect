from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy



"""
Cafés should have Wifi & Power 
(A Electrical outlet for laptop, 
phone, or anything that charge with power)
"""



db: SQLAlchemy = SQLAlchemy()
app: Flask = Flask(__name__)

class Cafe(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.Column(db.String(100), nullable=False))
    location: str = db.Column(db.Column(db.String(100), nullable=False))
    wifi: str = db.Column(db.Column(db.String(100), nullable=False))
    power: str =db.Column(db.Column(db.String(100), nullable=False))
    link: str =db.Column(db.Column(db.String(1000), nullable=False))


cafe: list[dict[str, str]] = [
    {"Name": "Brewed Awakening", "Location": "E 1st Ave", "Wifi": "⚡ 📶Yes", "Power": "🔌Yes", "Link": "https://www.google.com/"},
    {"Name": "Java Junction", "Location": "Clark Dr", "Wifi": "Yes", "Power": "No", "Link": "https://www.google.com/"}
    ]
cafe_titles: list[str] = [key for element in cafe for key, value in element.items()]


@app.route("/")
def index() -> str:
    return render_template("index.html", cafe_list=cafe, cafe_title=cafe_titles)

# Todo: Add function to store new good Cafés or Cafés
# Todo: Get information from the database
# Todo: (Maybe) getting more dynamic program that get all good Cafés base on user ip address.

if __name__ == "__main__":
    app.run(debug=True)
