from playsound3 import playsound
import time
import mysql.connector
from zoneinfo import ZoneInfo
from datetime import datetime,timedelta
def database():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="webpy"
        )
    except Exception as e:
        print(f"[RALAT] Sambungan gagal: {repr(e)}")
        return None

def sound():
    playsound(r"C:\Users\faris\OneDrive\Desktop\runstar\coin.mp3")
def updatestat(conn, iduser):
    cursor = conn.cursor()
    cursor.execute("UPDATE pengguna SET status = %s, masa_akhir = %s WHERE id = %s", ('0', '0000-00-00 00:00:00', iduser))
    conn.commit()
def main():
    while True:
        conn=database()
        if conn is None:
            print(f"Database tidak fungsi")
            continue
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM pengguna WHERE status = 1 AND masa_akhir != '00:00:00'")
        rows=cursor.fetchall()
        if rows:
            for row in rows:
                iduser = row[0]
                masaakhir = row[8]
                harini = datetime.now(ZoneInfo("Asia/Kuala_Lumpur")).strftime("%Y-%m-%d %H:%M:%S")
                print(f"Masa kini: {harini}, Masa Akhir: {masaakhir}") 
                if harini >= masaakhir:
                    print(f"sama")
                    sound()
                    updatestat(conn, iduser)
                    print(f"Berjaya Update")
                    time.sleep(1)
                else:
                    print(f"Tidak sama")
                    time.sleep(1)
        else:
            print(f"Tiada user")
            time.sleep(2)
            continue
if __name__ == "__main__":
    main()
