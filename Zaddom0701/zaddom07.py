# Imię i nazwisko

from flask import Flask, render_template
import json

app = Flask(__name__)


def load_json_data():
    with open('database.json') as f:
        return json.load(f)


@app.route('/')
def index():
    people_list = load_json_data()
    return render_template('people_list.html', people_list=people_list)


@app.route('/person/<int:index>')
def person(index):
    people_list = load_json_data()

    context = {}

    # tutaj napisz logikę wyciągającą odpowiednią osobę z `people_list`
    # ustaw `context` zgodnie z rezultatem wyszukiwania

    return render_template('person.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
