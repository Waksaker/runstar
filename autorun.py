import mysql.connector
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import time
import subprocess
def runtrade(username, password, iduser):
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
def runtransfer(username, password, iduser):
    filepython = r"C:\Users\faris\OneDrive\Desktop\runstar\venv\Scripts\python.exe"
    filerun = r"C:\Users\faris\OneDrive\Desktop\runstar\runtransfer.py"
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
def connect_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="webpy"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error Database: {err}")
        return None
def main():
    while True:
        conn = connect_database();
        if conn is None:
            print(f"Database tidak sambung")
            continue
        else:
            masakini = datetime.now(ZoneInfo("Asia/Kuala_Lumpur")).strftime('%H:%M:%S')
            print(f"Time: {masakini}")
            if (masakini >= '08:10:00') or (masakini <= '05:59:59'):
                print(f"Masuk waktu")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM pengguna WHERE trades != '0' AND status = '0' AND masa_akhir = '00:00:00'")
                row = cursor.fetchone()
                if row:
                    iduser = row[0]
                    username = row[1]
                    password = row[2]
                    print(f"Status: Run Trade, ID: {iduser}, Username: {username}, Password: {password}")
                    runtrade(username, password, iduser)
                    time.sleep(60)
                else:
                    cursor1 = conn.cursor()
                    cursor1.execute("""
                        SELECT 
                            * 
                        FROM 
                            pengguna
                        WHERE 
                            trades = '0' AND
                            status = '0' AND
                            masa_akhir = '00:00:00' AND
                            runtrans = '1'
                    """)
                    row1 = cursor1.fetchone()
                    if row1:
                        iduser = row1[0]
                        username = row1[1]
                        password = row1[2]
                        print(f"Status: Run Transfer, ID: {iduser}, Username: {username}, Password: {password}")
                        runtransfer(username, password, iduser)
                        time.sleep(60)
                    else:
                        print("Semua sudah selesai")
                        time.sleep(2)
            else:
                print(f"Luar waktu")
                break
if __name__=="__main__":
    main()