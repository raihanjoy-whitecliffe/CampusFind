from flask import Flask, render_template
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, template_folder="html")


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


@app.route("/signin")
def signin():
    return render_template("signin.html")


@app.route("/report")
def report():
    return render_template("Report.html")


if __name__ == "__main__":
    app.run(debug=True)