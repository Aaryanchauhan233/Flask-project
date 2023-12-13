from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'harshrajput...'
app.config['MYSQL_db'] = 'users'

mysql = MySQL(app)


@app.route('/')
def next():
    return "Enter --> /hello "


@app.route('/hello')
def hello_world():
    return render_template('index.html')


@app.route('/users')
def user():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users.users")
    fetchdata = cur.fetchall()
    cur.close()
    return render_template('users.html', data=fetchdata)


@app.route('/new_users', methods=['GET', 'POST'])
def new_users():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO users.users (name, email, role) VALUES(%s, %s, %s)', (name, email, role))
        mysql.connection.commit()
    return render_template('new_users.html')


# Custom error handler for 404 - Resource Not Found
@app.errorhandler(404)
def not_found_error(error):
    return "Resource not found.", 404


@app.route('/user/<int:user_id>')
def user_id(user_id):
    cur = mysql.connection.cursor()
    query = "SELECT id, name, email, role FROM users.users WHERE id = %s"
    data = (user_id,)
    cur.execute(query, data)
    fetchdata = cur.fetchall()
    cur.close()
    if user:
        return render_template('user_id.html', data=fetchdata)

    else:
        # If the user with the given ID is not found, trigger a 404 error
        return not_found_error(404)


app.run(debug=True)
