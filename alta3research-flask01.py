from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import redirect
from flask import session
from flask import jsonify

import requests

"""
https://github.com/csfeeser/Python/blob/master/TLG/flask_project.md

https://github.com/csfeeser/Python/blob/master/pyapi/flask_JSON_demo_API.md

Your script alta3research-flask01.py should demonstrate proficiency with the flask library. Ensure your application has:

at least two endpoints
at least one of your endpoints should return legal JSON
has ONE additional feature from the following list:
one endpoint returns HTML that uses jinja2 logic
requires a session value be present in order to get a legal response
writes to/reads from a cookie
reads from/writes to a sqlite3 database

TODO project reqs
[X] two endpoints
[X] one of your endpoints should return legal JSON
[X] has ONE additional feature from the following list:
    - one endpoint returns HTML that uses jinja2 logic
    - requires a session value be present in order to get a legal response
    - writes to/reads from a cookie
    - reads from/writes to a sqlite3 database

TODO what I want to implement
[ ] get sessions working for storing pokemon
[ ] clean up html/css
author Tomas
v1
"""

pokemon_list = {}
# MY SCRIPTS
# get pokemon  image url
url_pokemon_stats = "https://pokeapi.co/api/v2/pokemon/"


def get_pokemon_img(pokemon_name):
    response = requests.get(url_pokemon_stats + pokemon_name)
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_image = pokemon_data["sprites"]["front_default"]
    else:
        pokemon_image = "not a pokemon"
    return pokemon_image


app = Flask(__name__)

# FLASk
# session
app.secret_key = "secret phrase here"
# Main page


@app.route("/")
def index():
    if "username" in session:
        username = session["username"]
        # if "pokemon_list" in session:
        #     pokemon_list = session["pokemon_list"]
        print(f"Welcome Back {username}")
        print(session)
        return redirect(url_for("search", name=username))
    else:
        return render_template("index.html", page="login")



# login
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        if len(user) == 0:
            return render_template("index.html", page="login")
        else:
            session["username"] = request.form.get("username")
    return redirect(url_for("search", name=user))


@app.route("/search/<name>", methods=["POSTS", "GET"])
def search(name):
    return render_template("search.html", page="search", name=session["username"], pokemon_list=pokemon_list)


@app.route("/update", methods=["POST"])
def update():

    pokemon = request.form.get("pokemon")
    pokemon_data = get_pokemon_img(pokemon)
    if pokemon_data == "not a pokemon":
        return redirect("/search/" + session["username"])
    else:
        pokemon_list[pokemon] = pokemon_data
        # session["pokemon_list"].append(pokemon)

    return redirect("/search/" + session["username"])


@app.route("/clear", methods=["POST"])
def clear():
    # session["pokemon_list"].clear()
    pokemon_list.clear()
    return render_template("search.html", page="search", name=session["username"])


@app.route("/display_pokemon", methods=["POST", "GET"])
def display_pokemon():
    return jsonify(pokemon_list)


if __name__ == ("__main__"):
    app.run()
