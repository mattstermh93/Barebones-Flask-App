from app import app
from flask import render_template
from app.calculations import Calc

@app.route('/')
@app.route('/index')
def index():
    calc = Calc()
    return render_template('index.html', calc=calc)
