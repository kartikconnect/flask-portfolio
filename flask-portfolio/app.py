from flask import Flask, render_template, request, redirect, url_for
from main import main_blueprint  # Import your blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(main_blueprint, url_prefix='/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ml-demo', methods=['GET', 'POST'])
def ml_demo():
    # ML demo logic yahan par
    return render_template('ml_demo.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('submit'))  # Redirect to the 'submit' endpoint after form submission
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Process the form data (e.g., save to database, send email, etc.)
    print(f"Name: {name}, Email: {email}, Message: {message}")
    return redirect(url_for('thank_you'))

@app.route('/projects')
def projects():
    return render_template('projects.html')  # Ensure 'projects.html' exists in the templates folder

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')  # Ensure this template exists

if __name__ == '__main__':
    app.run(debug=True)
