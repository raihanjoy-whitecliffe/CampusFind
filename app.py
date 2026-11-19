from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.security import check_password_hash

# Load environment variables
load_dotenv(dotenv_path=".env", override=True)
app = Flask(__name__, template_folder="html")
app.secret_key = os.getenv("SECRET_KEY")

# MySQL database connection
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    return connection

#routes to all pages
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM Users WHERE email = %s",
            (email,)
        )

        user = cursor.fetchone()

        cursor.close()
        connection.close()

        if user and check_password_hash(user["password_hash"], password):

            session["user_id"] = user["user_id"]
            session["user_name"] = user["name"]

            return redirect(url_for("home"))

        return render_template(
            "signin.html",
            error="Invalid email or password. Please try again."
        )

    return render_template("signin.html")


@app.route("/report")
def report():
    return render_template("Report.html")

@app.route("/test-db")
def test_db():
    try:
        connection = get_db_connection()

        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM Users")

        user_count = cursor.fetchone()[0]

        cursor.close()
        connection.close()

        return f"MySQL Connected! Total users: {user_count}"

    except Exception as e:
        return f"Database Connection Failed: {e}"
    
if __name__ == "__main__":
    app.run(debug=True)