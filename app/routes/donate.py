# These routes are an example of how to use data, forms and routes to create
# a forum where a posts and comments on those posts can be
# Created, Read, Updated or Deleted (CRUD)

from flask.helpers import url_for
from app import app, login
import mongoengine.errors
from flask import render_template, flash, redirect
from flask_login import current_user
from app.classes.data import Donate
from app.classes.forms import Donation
from flask_login import login_required
import datetime as dt

@app.route('/donation', methods=['GET', 'DONATION'])
@login_required

def donation2():
    form = Donation()

    if form.validate_on_submit():

        newDonation = Donation(
            money = form.money.data,
            author = current_user.id,
        )
        # This is a metod that saves the data to the mongoDB database.
        newDonation.save()

        return redirect(url_for('donation',donationID=newdonation.id))

    return render_template('donation.html',form=form)