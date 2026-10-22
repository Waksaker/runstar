from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

app = Flask(__name__)

def connect_database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

@app.route("/")
def index():
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
    return redirect(url_for('index'))

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

@app.route('/app/user')
def get_users():
    try:
        db = connect_database()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM pengguna")
        rows = cursor.fetchall()
        
        for row in rows:
            # Tukar DATETIME/TIMESTAMP ke teks
            if row.get('created_at'):
                row['created_at'] = row['created_at'].strftime("%Y-%m-%d %H:%M:%S")
            if row.get('updated_at'):
                row['updated_at'] = row['updated_at'].strftime("%Y-%m-%d %H:%M:%S")
            
            # Tukar masa_akhir — pastikan betul-betul jadi teks
            if row.get('masa_akhir') is not None:
                val = row['masa_akhir']
                if isinstance(val, timedelta):
                    # Tukar timedelta ke format HH:MM:SS
                    total_saat = int(val.total_seconds())
                    jam = total_saat // 3600
                    minit = (total_saat % 3600) // 60
                    saat = total_saat % 60
                    row['masa_akhir'] = f"{jam:02d}:{minit:02d}:{saat:02d}"
                else:
                    row['masa_akhir'] = str(val)
        
        cursor.close()
        db.close()
        return jsonify({'users': rows})
    
    except Exception as e:
        print(f"❌ Ralat di /app/user: {repr(e)}")
        return jsonify({'error': str(e), 'users': []}), 500

@app.route('/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    conn = connect_database()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        trades = request.form['trades']
        status = request.form['status']
        transfer = request.form['transfer']

        cursor.execute(
            "UPDATE pengguna SET username=%s, password=%s, trades=%s, status=%s, statranfer=%s, runtrans=%s WHERE id=%s",
            (username, password, trades, status, transfer, transfer, user_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        # Pastikan guna nama yang BETUL
        return redirect(url_for("index"))  # ✅ atau url_for("index") jika dah tetapkan endpoint
    
    cursor.execute("SELECT * FROM pengguna WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit.html', user=user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
