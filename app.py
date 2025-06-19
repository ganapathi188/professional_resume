from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to XAMPP MySQL (adjust credentials as needed)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="resume_db"
)
cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        cell = request.form['cell']
        email = request.form['email']
        address = request.form['address']
        cursor.execute("INSERT INTO contact (name, cell, email, address) VALUES (%s, %s, %s, %s)", 
                       (name, cell, email, address))
        db.commit()
        return "Message Sent Successfully!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)