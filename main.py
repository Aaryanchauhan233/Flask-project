# app.py
from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Replace 'your_database', 'your_username', 'your_password', and 'your_host' with your actual MySQL configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harshrajput147",
    database="users"
)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        # Get user input from the form
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        # Save the user information in the database
        cursor = db.cursor()
        query = "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)"
        data = (name, email, role)
        cursor.execute(query, data)
        db.commit()

        # Redirect to a success page or homepage after saving the user
        return "User data successful store!"

    # Render the new_user.html template for GET requests
    return render_template('new_users.html')

if __name__ == '__main__':
    app.run(debug=True)
