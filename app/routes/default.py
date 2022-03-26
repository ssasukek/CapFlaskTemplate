from app import app
from flask import render_template

# This is for rendering the home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/climatechange')
def climatechange():
    return render_template('climatechange.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/jerryideas')
def jerryideas():
    return render_template('jerryideas.html')