from playsound3 import playsound
import time
import mysql.connector
from zoneinfo import ZoneInfo
from datetime import datetime,timedelta
def database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    return mysql.connector.connect(host=host, user=user, password=password, database=database)
def sound():
    playsound(r"C:\Users\faris\OneDrive\Desktop\runstar\coin.mp3")
def updatestat(conn, iduser):
    cursor = conn.cursor()
    cursor.execute("UPDATE pengguna SET status = %s, masa_akhir = %s WHERE id = %s", ('0', '00:00:00', iduser))
    conn.commit()
def main():
    while True:
        conn=database()
        cursor=conn.cursor()
        cursor.execute("SELECT * FROM pengguna WHERE status = 1 AND masa_akhir != '00:00:00'")
        rows=cursor.fetchall()
        for row in rows:
            iduser=row[0]
            masaakhir=row[7]
            hari_ini=datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))
            masakini_obj = hari_ini
            h, m, s = map(int, masaakhir.split(':'))
            masaakhir_obj = hari_ini.replace(hour=h, minute=m, second=s, microsecond=0)
            if masaakhir_obj < masakini_obj:
                masaakhir_obj = masakini_obj
                print(f"Masa {masaakhir} sudah lepas hari ni -> terus proses")
            else:
                print(f"Tunggu masa {masaakhir} hari ini")
            print(f"Id User: {iduser}, Masa Kini: {masakini_obj.strftime('%H:%M:%S')}, Masa Akhir: {masaakhir_obj.strftime('%H:%M:%S')}") 
            if masakini_obj >= masaakhir_obj:
                print(f"sama")
                sound()
                updatestat(conn, iduser)
                print(f"Berjaya Update")
                time.sleep(2)
            else:
                print(f"Tidak sama")
                time.sleep(2)
if __name__ == "__main__":
    main()
