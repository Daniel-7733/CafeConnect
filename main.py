from flask import Flask, render_template, request, flash, redirect, Response, url_for
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
db_path: str = path.join(app.instance_path, "cafe.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


class Cafe(db.Model):
    __tablename__ = "cafe"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    location: str = db.Column(db.String(100), nullable=False)
    wifi: str = db.Column(db.String(100), nullable=False)
    power: str = db.Column(db.String(100), nullable=False)
    link: str = db.Column(db.String(1000), nullable=False)


db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def index() -> str:
    """
    Load main page in html & show all the cafe.

    :return: (str) index.html
    """

    cafe: list[Cafe] = Cafe.query.all()
    return render_template("index.html", cafe_list=cafe)


def is_it_same(link: str) -> bool:
    """
    Check if data exist in database.

    :return: (bool) True if data exist otherwise false
    """
    return db.session.query(Cafe).filter_by(link=link).first() is not None

@app.route("/add-cafe", methods=["GET", "POST"])
def add_all() -> Response | str:
    """
    Load the second page for adding cafe in to the database.

    :return: (str | Response) cafeAdmin.html.
    """

    if request.method == "POST":
        name: str = request.form["name"]
        location: str = request.form["location"]
        link: str = request.form["link"]

        check: bool = is_it_same(link=link)

        if check:
            flash("Same Cafe", "error")
            return redirect(url_for("add_all"))
        else:
            cafe_info = Cafe(
                name=name,
                location=location,
                wifi="📶",
                power="🔋",
                link=link
            )

            db.session.add(cafe_info)
            db.session.commit()
            flash("Cafe Successfully added.", "success")
            return redirect(url_for("index"))
    else:
        return render_template("cafeAdmin.html")


if __name__ == "__main__":
    app.run(debug=True)
