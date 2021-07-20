from flask_app import app
from flask import render_template, redirect, session, request

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_survey', methods = ["POST"])
def create():
    if not Dojo.validate_survey(request.form):
        return redirect('/')
    Dojo.create_dojo_survey(request.form)
    return redirect('/results')

@app.route('/results')
def results():
    survey = Dojo.get_survey()
    return render_template('results.html', survey = survey)