from flask import Blueprint, render_template, request, redirect, url_for

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():
    return render_template('index.html')

@main_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data (e.g., save to database, send email, etc.)
        print(f"Name: {name}, Email: {email}, Message: {message}")
        return redirect(url_for('main.thank_you'))
    return render_template('contact.html')

@main_blueprint.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')
