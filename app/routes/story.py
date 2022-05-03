from flask.helpers import url_for
from app import app
from flask import render_template
from app.classes.data import Page
from app.classes.forms import PageForm
import mongoengine.errors
from flask import render_template, flash, redirect
from bson import ObjectId

@app.route("/page/list")
def pageList():
    pages = Page.objects()
    return render_template('/CYOA/pages.html', pages=pages)

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
            content = form.content.data,
            c1 = form.c1.data,
            c2 = form.c2.data,
            c3 = form.c3.data,
        )
        # This is a metod that saves the data to the mongoDB database.
        newPage.save()
        newPage.reload()
        if form.image.data:
            newPage.image.put(form.image.data, content_type = 'image/jpg')
            # This saves all the updates
            newPage.save()

        return redirect(url_for('page',pageID=newPage.id))

    return render_template('/CYOA/pageform.html',form=form)

@app.route("/page/delete/<pageId>")
def pageDelete(pageId):
    pageDelete = Page.objects.get(id=pageId)
    pageDelete.delete()
    flash("The page was deleted.")
    return redirect(url_for('pageList'))

@app.route('/page/edit/<pageId>', methods=['GET', 'POST'])
# This is a function that is run when the user requests this route.
def pageEdit(pageId):
    # This gets a form object that can be displayed on the template
    form = PageForm()
    editPage = Page.objects.get(id=pageId)
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
        editPage.update(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            title = form.title.data,
            directions = form.directions.data,
            content = form.content.data,
            c1 = ObjectId(form.c1.data),
            c2 = ObjectId(form.c2.data),
            c3 = ObjectId(form.c3.data)
        )
        # This is a metod that saves the data to the mongoDB database.
        editPage.reload()
        if form.image.data:
            if editPage.image:
                editPage.image.delete()
            editPage.image.put(form.image.data, content_type = 'image/jpg')
            # This saves all the updates
            editPage.save()
    

        return redirect(url_for('page',pageID=editPage.id))

    try: 
        editPage.c1
    except:
        pass
    else:
        form.c1.default = editPage.c1.id
    try: 
        editPage.c2
    except:
        pass
    else:
        form.c2.default = editPage.c2.id
    try: 
        editPage.c3
    except:
        pass
    else:
        form.c3.default = editPage.c3.id
    form.process()


    form.title.data = editPage.title
    form.directions.data = editPage.directions
    form.content.data = editPage.content
    form.image.data = editPage.image
    return render_template('/CYOA/pageform.html',form=form, page=editPage)