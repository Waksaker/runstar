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
def run(iduser, username, password):
    filepython = r"C:\Users\faris\OneDrive\Desktop\runstar\venv\Scripts\python.exe"
    filerun = r"C:\Users\faris\OneDrive\Desktop\runstar\runprofit.py"
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
        return
def updatefunc(func):
    try:
        conn = connect_database()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE
                `func`
            SET
                `func` = %s
            WHERE 
                `id` = %s
        """, (func, 1))
        conn.commit()
    except Exception as e:
        print(f"Ralat semasa mengemaskini function: {repr(e)}")
def main():
    while True:
        conn = connect_database()
        if conn is None:
            print(f"Sambungan databse gagal")
            time.sleep(1)
            continue
        else:
            updatefunc(4)
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    * 
                FROM
                    pengguna
                WHERE
                    trades = '0' AND
                    status = '0' AND
                    masa_akhir = '0000-00-00 00:00:00' AND
                    runtrans = '0' AND
                    staprofit = '1' 
            """)
            row = cursor.fetchone()
            if row:
                iduser = row[0]
                username = row[1]
                password = row[2]
                print(f"ID: {iduser}, USERNAME: {username}, PASSWORD: {password}")
                run(iduser, username, password)
                time.sleep(60)
            else:
                print(f"TIADA USER")
                updatefunc(0)
                time.sleep(2)
                break
if __name__ == "__main__":
    main()
