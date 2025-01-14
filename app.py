from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'
app.config['MYSQL_DB'] = 'w3schools'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template('home.html', titolo='Home Page')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'GET':
        return render_template('register.html', titolo='Register')
    else:
        #print("SONO QUI")
        nome = request.form.get("nome")
        cognome = request.form.get("cognome")
        username = request.form.get("username")
        password = request.form.get('password')
        confermaPassword = request.form.get('confermaPassword')
        
        
        query = "INSERT INTO users VALUES (%s,%s,%s,%s)"
        cursor = mysql.connection.cursor()
        cursor.execute(query, (username,password,nome,cognome))
        mysql.connection.commit()
        return redirect('/')

@app.route("/login")
def login():
    return render_template('login.html', titolo='Login')

@app.route("/logout")
def logout():
    return render_template('logout.html', titolo='Logout')




app.run(debug=True)
