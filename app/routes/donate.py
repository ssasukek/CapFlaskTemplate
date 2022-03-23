# These routes are an example of how to use data, forms and routes to create
# a forum where a posts and comments on those posts can be
# Created, Read, Updated or Deleted (CRUD)

from flask.helpers import url_for
from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect
from flask_login import current_user
from app.classes.data import Donate
from app.classes.forms import DonateForm
from flask_login import login_required
import datetime as dt 

# This is the route to list all posts
@app.route('/donation')
# This means the user must be logged in to see this page
@login_required
def donationList():
    # This retrieves all of the 'posts' that are stored in MongoDB and places them in a
    # mongoengine object as a list of dictionaries name 'posts'.
    donates = Donate.objects()
    # This renders (shows to the user) the posts.html template. it also sends the posts object 
    # to the template as a variable named posts.  The template uses a for loop to display
    # each post.
    return render_template('donation.html',donation=Donate)

# This route renders a form for the user to create a new post
@app.route('/donation', methods=['GET', 'DONATE'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def donationNew():
    # This gets a form object that can be displayed on the template
    form = DonateForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new post form. 
        # Post() is a method for creating a new post. 'newPost' is the variable where the object
        # that is the result of the Post() method is stored.  
        newDonation = Donate(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            # subject = form.subject.data,
            # content = form.content.data,
            # rate_game = form.rate_game.data,
            author = current_user.id,
            # This sets the modifydate to the current datetime.
            modifydate = dt.datetime.utcnow
        )
        # This is a metod that saves the data to the mongoDB database.
        newDonation.save()

        return redirect(url_for('Donate',donateID=newDonation.id))

    return render_template('donation.html',form=form)

@app.route('/donate/<donateID>')
@login_required
def donate(donateID):
    donate = Donate.objects.get(id=donateID)

    return render_template('donation.html',donate=donate)
