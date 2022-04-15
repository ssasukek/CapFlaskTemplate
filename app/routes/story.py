from app import app
from flask import render_template
from app.classes.data import Page

@app.route("/page/list")
def pageList():
    pages = Page.objects()
    return render_template('pages.html')

@app.route("/page/<pageID>")
def page(pageID):
    thisPage = Page.objects.get(id=pageID)
    return render_template("page.html",thisPage=thisPage)

