import mysql.connector
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
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
def main():
    while True:
        conn = connect_database();
        if conn is None:
            print(f"Database tidak sambung")
            continue
        else:
            masakini = datetime.now(ZoneInfo("Asia/Kuala_Lumpur")).strftime('%H:%M:%S')
            print(f"Time: {masakini}")
            if masakini >= '08:10:00' and masakini <= '23:59:59':
                print(f"Masuk masa")
            else:
                print(f"Luar waktu")
                break
            time.sleep(2)
if __name__=="__main__":
    main()