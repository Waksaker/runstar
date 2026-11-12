import mysql.connector
import time
import subprocess
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
            print("Gagal connect database. Cuba semula...")
            time.sleep(5)
            continue
        try:
            updatefunc(3)
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT 
                    *
                FROM
                    pengguna
                WHERE
                    trades = '0' AND
                    status = '0' AND
                    masa_akhir = '0000-00-00 00:00:00' AND
                    runtrans = '1'
            """)
            row = cursor.fetchone()
            if row:
                username = row['username']
                password = row['password']
                iduser = row['id']
                run(username, password, iduser)
                time.sleep(60)
                continue
            else:
                print("Tiada pengguna dengan runtrans =1")
                updatefunc(0)
                cursor.close()
                conn.close()
                break
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(f"Masalah Database: {err}")
            break
        time.sleep(2)
        continue
if __name__ == "__main__":
    main()
