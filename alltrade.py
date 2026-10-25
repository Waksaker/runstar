import mysql.connector
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time
import subprocess
def connect_database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    try:
        return mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
    except Exception as e:
        print(f"[RALAT] Sambungan gagal: {repr(e)}")
        return None
def runtrade(username, password, iduser):
    print(f"username: {username}, password: {password}, ID user: {iduser}")
    filepython = r"C:\Users\faris\OneDrive\Desktop\runstar\venv\Scripts\python.exe"
    filerun = r"C:\Users\faris\OneDrive\Desktop\runstar\runtrade.py"
    try:
        result = subprocess.run(
            [filepython, filerun, str(username), str(password), str(iduser)],
            capture_output=True,  # Tangkap output supaya tidak bersepah di terminal
            text=True,            # Tukar output dari bytes kepada string biasa
            check=True            # Baling error jika skrip gagal
        )
        print(f"[SUKSES] Skrip untuk id {iduser} berjaya dijalankan.")
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Skrip run untuk id {iduser} gagal.")
        print("Detail Error:", e.stderr)
def main():
    while True:
        conn=connect_database()
        if conn is None:
            print(f"Sambungan databse gagal")
            time.sleep(1)
            continue
        else:
          #  print(f"Sambungan database berjaya")
            time.sleep(1)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT
                    *
                FROM
                    pengguna
                WHERE
                    trades != 0 AND
                    status = 0
            """)
            row = cursor.fetchone()
            if row:
                username = row['username']
                password = row['password']
                iduser = row['id']
                runtrade(username, password, iduser)
                time.sleep(60)
                continue
            else:
                print(f"Tiada user")
                time.sleep(2)
                cursor.close()
                conn.close()
                break
if __name__ == "__main__":
    main()
