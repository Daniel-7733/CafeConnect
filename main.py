from flask import Flask, render_template

"""Cafés should have Wifi & Power (A Electrical outlet for laptop, phone, or anything that charge with power)"""


cafe: list[dict[str, str]] = [
    {"Name": "Brewed Awakening", "Location": "E 1st Ave", "Wifi": "Yes", "Power": "Yes", "Link": "https://www.google.com/"},
    {"Name": "Java Junction", "Location": "Clark Dr", "Wifi": "Yes", "Power": "No", "Link": "https://www.google.com/"}
    ]


app: Flask = Flask(__name__)

@app.route("/")
def index() -> str:
    return render_template("index.html", cafe_list=cafe)

# Todo: Add function to store new good Cafés or Cafés
# Todo: Get information from the database
# Todo: (Maybe) getting more dynamic program that get all good Cafés base on user ip address.

if __name__ == "__main__":
    app.run(debug=True)
