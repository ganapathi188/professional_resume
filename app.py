from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('resume.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cell TEXT NOT NULL,
            email TEXT NOT NULL,
            address TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()  # Ensure DB is ready on startup

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

        conn = sqlite3.connect('resume.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO contact (name, cell, email, address) VALUES (?, ?, ?, ?)",
                       (name, cell, email, address))
        conn.commit()
        conn.close()

        return "Message Sent Successfully!"
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)