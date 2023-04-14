from flask import Blueprint, render_template, redirect, url_for, send_file

blueprint = Blueprint('simple_pages', __name__, template_folder='.../templates'

@blueprint.route('/')
def index():
    return render_template('index.html')

@blueprint.route('/about')
def about():
    return render_template("travel.html")
    

@blueprint.route('/food')
def about_blog():
    return redirect(food.html)

@blueprint.route('/legal')
def legal():
    return send_file('static/downloads/legal.txt', as_attachment=True)