from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/submit_survey', methods=['POST'])
def submit_survey():
    # Get the form data from the request
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    education = request.form['education']
    interests = ', '.join(request.form.getlist('interests'))
    comments = request.form['comments']
    
    # Store the data in a SQLite database
    conn = sqlite3.connect('survey.db')
    c = conn.cursor()
    c.execute('INSERT INTO responses (name, age, gender, education, interests, comments) VALUES (?, ?, ?, ?, ?, ?)', (name, age, gender, education, interests, comments))
    conn.commit()
    conn.close()
    
    # Redirect the user to a thank you page
    return render_template('thank_you.html')
