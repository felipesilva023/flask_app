from flask import Flask, render_template, request
from search import print_vowels

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Bem vindos ao buscador de vogais'


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Bem vindos ao buscador de vogais')


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    return str(print_vowels(phrase))


app.run(debug=True)
