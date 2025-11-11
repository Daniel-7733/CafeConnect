from flask import Flask, render_template, request, flash
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
    link: str = db.Column(db.String(1000), nullable=False)


cafe: list[dict[str, str]] = [
    # These are just example and may not have any power and internet however cafés does exist.
    {"Name": "Brewed Awakening", "Location": "E 1st Ave", "Wifi": "📶", "Power": "🔌", "Link": "https://www.brewedawakening.com/"},
    {"Name": "cafe Medina", "Location": "Clark Dr", "Wifi": "📶", "Power": "🔌", "Link": "https://www.medinacafe.com/"},
    {"Name": "Kennington Lane Cafe", "Location": "Londen", "Wifi": "📶", "Power": "🔌", "Link": "https://cafekenningtonlane.co.uk/"},
    {"Name": "Sheila's Cafe", "Location": "Londen", "Wifi": "📶", "Power": "🔌", "Link": "https://sheilas.cafe/"},
    {"Name": "cafe Medina", "Location": "Clark Dr", "Wifi": "📶", "Power": "🔌", "Link": "https://www.medinacafe.com/"},
    {"Name": "PROJECT68", "Location": "London (near King’s Cross / Russell Square)", "Wifi": "📶", "Power": "🔌", "Link": "https://laptopfriendlycafe.com/cafes/london/project68"},
    {"Name": "Caffe Mira", "Location": "3136 Main St, Vancouver BC, Canada", "Wifi": "📶", "Power": "🔌", "Link": "https://laptopfriendlycafe.com/cafes/vancouver/caffe-mira"},
    {"Name": "AVIK Cafe", "Location": "Vancouver BC, Canada", "Wifi": "📶", "Power": "🔌", "Link": "https://laptopfriendlycafe.com/cafes/vancouver/avik"},
    {"Name": "Café Z Bar", "Location": "58 Stoke Newington High St, London N16 7PB", "Wifi": "📶", "Power": "🔌", "Link": "https://laptopfriendly.co/london/cafe-z-bar"},
    {"Name": "Basecamp Coffee Shop", "Location": "Seattle, WA, USA", "Wifi": "📶", "Power": "🔌", "Link": "https://awifiplace.com/cafes/basecamp-coffee-shop-seattle"}
    ]

@app.route("/")
def index() -> str:
    return render_template("index.html", cafe_list=cafe)


@app.route("/show-all-cafe")
def show_all() -> str:
    cafes: list[Cafe] = Cafe.query.all()
    return render_template("cafeAdmin.html", cafes=cafes)


@app.route("/add-cafe", methods=["GET", "POST"])
def add_all() -> str:
    if request.method == "POST":
        name: str = request.form["name"]
        location: str = request.form["location"]
        wifi: str = request.form["wifi"]
        power: str = request.form["power"]
        link: str = request.form["link"]

        cafe_info: Cafe = Cafe(
            name=name,
            location=location,
            wifi=wifi,
            power=power,
            link=link
        )

        db.session.add(cafe_info)
        db.session.commit()
        flash("Cafe Successfully add it.", "error") # it is not implemented in html yet
    else:
        flash("Fail to add.", "error")

    return render_template("cafeAdmin.html")

if __name__ == "__main__":
    app.run(debug=True)
