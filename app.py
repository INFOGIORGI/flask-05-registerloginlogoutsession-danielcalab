from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "AudiS3"
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
        
        #Controllo password=confermaPassword
        if password==confermaPassword:     
            #Controllo username non in uso
            querySelect = "SELECT * FROM users WHERE username=%s"
            cursor = mysql.connection.cursor()
            cursor.execute(querySelect, (username,))
            data = cursor.fetchall()

            if len(data)<1:
                #Inserimento nel DB
                query = "INSERT INTO users VALUES (%s,%s,%s,%s)"
                cursor.execute(query, (username,generate_password_hash(password),nome,cognome))
                mysql.connection.commit()
                return redirect(url_for('register'))
            else:
                flash("Username già presente")
                return redirect(url_for('register'))
        else:
            flash("Le password non corrispondono")
            return redirect(url_for('register'))


@app.route("/login")
def login():
    return render_template('login.html', titolo='Login')

@app.route("/logout")
def logout():
    return render_template('logout.html', titolo='Logout')




app.run(debug=True)
