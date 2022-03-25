# These routes are an example of how to use data, forms and routes to create
# a forum where a donations and comments on those donations can be
# Created, Read, Updated or Deleted (CRUD)

from flask.helpers import url_for
from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect
from flask_login import current_user
from app.classes.data import Donations
from app.classes.forms import DonationForm
from flask_login import login_required
import datetime as dt 

@app.route('/donation/list')
# This means the user must be logged in to see this page
@login_required
def donationList():
    # This retrieves all of the 'posts' that are stored in MongoDB and places them in a
    # mongoengine object as a list of dictionaries name 'posts'.
    Donation = Donations.objects()
    # This renders (shows to the user) the posts.html template. it also sends the posts object 
    # to the template as a variable named posts.  The template uses a for loop to display
    # each post.
    return render_template('donation.html',donation=donation)

# This route renders a form for the user to create a new donation
@app.route('/donation/new', methods=['GET', 'DONATION'])
# This means the user must be logged in to see this page
@login_required
# This is a function that is run when the user requests this route.
def donationNew():
    # This gets a form object that can be displayed on the template
    form = DonationForm()

    # This is a conditional that evaluates to 'True' if the user submitted the form successfully 
    if form.validate_on_submit():

        # This stores all the values that the user entered into the new donation form. 
        # donation() is a method for creating a new donation. 'newdonation' is the variable where the object
        # that is the result of the donation() method is stored.  
        newDonation = Donations(
            # the left side is the name of the field from the data table
            # the right side is the data the user entered which is held in the form object.
            subject = form.subject.data,
            content = form.content.data,
            money = form.money.data,
            author = current_user.id,
            # This sets the modifydate to the current datetime.
            modifydate = dt.datetime.utcnow
        )
        # This is a metod that saves the data to the mongoDB database.
        newDonation.save()

        return redirect(url_for('donation',donationID=newDonation.id))

    return render_template('donation.html',form=form)

@app.route('/donation/<donationID>')
@login_required
def donation(donationID):
    donation = Donations.objects.get(id=donationID)

    return render_template('donation.html',donation=donation)

@app.route('/donation/delete/<donationID>')
@login_required
def donationDelete(donationID):
    deleteDonation = Donations.objects.get(id=donationID)
    if current_user == deleteDonation.author:
        deleteDonation.delete()
        flash('The donation was deleted.')
    else:
        flash("You can't delete a donation you don't own.")
    donations = donation.objects()  
    return render_template('donations.html',donations=donations)

@app.route('/donation/edit/<donationID>', methods=['GET', 'DONATION'])
@login_required
def donationEdit(donationID):
    editDonations = Donations.objects.get(id=donationID)
    if current_user != editDonations.author:
        flash("You can't edit a donation you don't own.")
        return redirect(url_for('donation',donationID=donationID))
    form = DonationForm()
    if form.validate_on_submit():
        editDonations.update(
            subject = form.subject.data,
            content = form.content.data,
            money = form.money.data,
            modifydate = dt.datetime.utcnow
        )
        return redirect(url_for('donation',donationID=donationID))

    form.subject.data = editDonations.subject
    form.content.data = editDonations.content
    form.money.data = editDonations.money

    return render_template('donationform.html',form=form)