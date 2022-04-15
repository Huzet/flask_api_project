import requests
from pprint import pprint

"""
https://github.com/csfeeser/Python/blob/master/TLG/flask_project.md

https://github.com/csfeeser/Python/blob/master/pyapi/flask_JSON_demo_API.md

Your script alta3research-requests02.py should demonstrate proficiency with the requests HTTP library. This script should:

send a GET request to your Flask API; it should target the endpoint that returns legal JSON.
take the returned JSON and "normalize" it into a format that is easy for users to understand.

TODO
[X] send a GET request to your Flask API; it should target the endpoint that returns legal JSON.
[X] take the returned JSON and "normalize" it into a format that is easy for users to understand.

author Tomas
v1
"""

url_pokemon_json = "http://127.0.0.1:5000/display_pokemon"

def get_pokemon_json():
    response = requests.get(url_pokemon_json)
    if response.status_code == 200:
        pokemon_json = response.json()
        pprint(pokemon_json)
    else:
        print("Please try again")
    return pokemon_json

def main():
    get_pokemon_json()

if __name__ == "__main__":
    main()