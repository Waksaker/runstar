import mysql.connector
import time
import subprocess

def connect_database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def run(username, password, iduser):
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
        return

def main():
    while True:
        try:
            conn = connect_database()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    *
                FROM
                    pengguna
                WHERE
                    runtrans = 1
            """)
            row = cursor.fetchone()
            if row:
                username = row['username']
                password = row['password']
                iduser = row['id']
                run(username, password, iduser)
            else:
                print("Tiada pengguna dengan runtrans =1")
                cursor.close()
                conn.close()
                break
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Masalah Database: {err}")
            break
        time.sleep(180)

if __name__ == "__main__":
    main()
