from flask.helpers import url_for
from app import app
from flask import render_template
from app.classes.data import Page
from app.classes.forms import PageForm
import mongoengine.errors
from flask import render_template, flash, redirect

@app.route("/page/list")
def pageList():
    page = Page.objects()
    return render_template('/CYOA/pages.html', page=page)

@app.route("/page/<pageID>")
def page(pageID):
    page = Page.objects.get(id=pageID)
    choices = []
    try:
        choices.append(page.c1)
    except:
        choices.append("None")
    try:
        choices.append(page.c2)
    except:
        choices.append("None")
    try:
        choices.append(page.c3)
    except:
        choices.append("None")
    
    return render_template("/CYOA/page.html",page=page,choices=choices)

@app.route('/page/new', methods=['GET', 'POST'])

# This is a function that is run when the user requests this route.
def pageNew():
    # This gets a form object that can be displayed on the template
    form = PageForm()
    pages = Page.objects()
    pageChoices = [(" ", " ")]

    for page in pages:
        pageChoices.append((page.id,page.title))
    form.c1.choices=pageChoices 
    form.c2.choices=pageChoices
    form.c3.choices=pageChoices

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new page form. 
        # page() is a method for creating a new page. 'newpage' is the variable where the object
        # that is the result of the page() method is stored.  
        newPage = Page(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            title = form.title.data,
            directions = form.directions.data,
            image = form.image.data,
            content = form.content.data,
            c1 = form.c1.data,
            c2 = form.c2.data,
            c3 = form.c3.data,
        )
        # This is a metod that saves the data to the mongoDB database.
        newPage.save()

        return redirect(url_for('page',pageID=newPage.id))

    return render_template('/CYOA/pageform.html',form=form)