from app import app
from flask import Flask, render_template



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
def solutions_get():
    return render_template('solutions.html')

if __name__ == "__main__":
    app.run(debug = True)


@app.route('/HI')
def humanInter():
    return render_template('humanInter.html')

@app.route('/blank')
def blank():
    return render_template('blank.html')


