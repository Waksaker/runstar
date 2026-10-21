from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from datetime import datetime
from zoneinfo import ZoneInfo

app = Flask(__name__)

def connect_database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

@app.route("/")
def home():
    db = connect_database()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM link")
    rows = cursor.fetchall()
    link = rows[0]['name'] if rows else ""
    cursor.close()
    db.close()
    return render_template(
        "index.html", 
        link=link
    )

@app.route("/submit", methods=["POST"])
def submit():
    db = connect_database()
    cursor = db.cursor()
    # Get the link from the form submission
    link = request.form.get("link")
    # Insert the link into the database
    cursor.execute("UPDATE link SET name = %s WHERE id = 1", (link,))
    db.commit()
    db.close()
    return redirect(url_for("home"))

@app.route('/app/masa')
def masa():
    waktu_msia = datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))
    tarikh = waktu_msia.strftime("%Y-%m-%d")
    time = waktu_msia.strftime("%H:%M:%S")
    db = connect_database()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT
            COUNT(*) AS jumlah_pengguna,
            SUM(CASE WHEN status = 1 THEN 1 ELSE 0 END) AS jumlah_running
        FROM pengguna
    """)
    rows = cursor.fetchall()
    jumlah_pengguna = rows[0]['jumlah_pengguna'] if rows else ""
    jumlah_running = rows[0]['jumlah_running'] if rows else ""
    cursor.close()
    db.close()
    return jsonify({
        'jumlah_pengguna': jumlah_pengguna,
        'jumlah_running': jumlah_running,
        'tarikh': tarikh,
        'time': time
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
