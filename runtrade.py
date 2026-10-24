import undetected_chromedriver as uc
import time
import mysql.connector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

def connect_database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

def updateruntrade(id_input):
    conn = connect_database()
    time = (datetime.now(ZoneInfo("Asia/Kuala_Lumpur"))+timedelta(hours=3)).strftime('%H:%M:%S')
    cursor = conn.cursor(dictionary=True)
    cursor1 = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM pengguna WHERE id=%s", (id_input,))
    rows = cursor.fetchone()
    trade = rows['trades']
    total = trade - 1
    cursor1.execute("UPDATE pengguna SET trades=%s, status=%s, masa_akhir=%s WHERE id=%s", (total, 1, time, id_input))
    conn.commit()
    cursor.close()
    cursor1.close()
    conn.close()

def main():
    db = None
    cursor = None
    driver = None

    if len(sys.argv) > 1:
        username_input = sys.argv[1]
        password_input = sys.argv[2]
        id_input = sys.argv[3]
    else:
        print("Sila berikan nama pengguna, kata laluan, dan ID sebagai argumen.")
        return

    try:
        db = connect_database()
        cursor = db.cursor(dictionary=True)

        cursor.execute("SELECT name FROM link LIMIT 1")
        row = cursor.fetchone()

        if not row or not row["name"]:
            print("URL tidak dijumpai dalam jadual link.")
            return

        link = row["name"].rstrip("/")
        url_index = f"{link}/index.php"
        url_checkin = f"{link}/checkin.php"
        url_trade = f"{link}/trade.php"
        url_logout = f"{link}/settings.php"

        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = uc.Chrome(
            option=options,
            version_main=155,
            supprress_welcome=True,
            headless=False
        )
        driver.get(url_index)

        time.sleep(3)

        # Tetapkan zoom selepas halaman mula dimuatkan
        driver.execute_script(
            "document.body.style.zoom = '50%'"
        )

        print("Tajuk laman:", driver.title)
        print("URL semasa:", driver.current_url)

        # === BAHAGIAN KLIK BUTANG BAHASA ===
        try:
            # Tunggu butang sedia & cari berdasarkan atribut data-lang="en"
            wait = WebDriverWait(driver, 15)
            lang_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button.lang-btn[data-lang="en"]')
                )
            )
            # Tatal ke butang jika tersembunyi
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", lang_btn)
            time.sleep(0.5)
            lang_btn.click()
            print("Berjaya mengklik butang MY/EN English")
            time.sleep(1)
        except Exception as e:
            print(f"Gagal mengklik butang: {repr(e)}")
        # === TAMAT BAHAGIAN KLIK ===

        # === 2. ISI NAMA PENGGUNA ===
        try:
            wait = WebDriverWait(driver, 15)
            username_field = wait.until(
                EC.presence_of_element_located((By.ID, "loginUser"))
            )
            username_field.clear()
            username_field.send_keys(username_input)
            print(f"Nama pengguna dimasukkan: {username_input}")
        except Exception as e:
            print(f"Gagal isi nama pengguna: {repr(e)}")

        # === 3. ISI KATA LALUAN ===
        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.ID, "loginPass"))
            )
            password_field.clear()
            password_field.send_keys(password_input)
            print("Kata laluan dimasukkan")
        except Exception as e:
            print(f"Gagal isi kata laluan: {repr(e)}")

        # === 4. KLIK BUTANG SIGN IN ===
        try:
            signin_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "loginSubmitBtn"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", signin_btn)
            time.sleep(0.5)
            signin_btn.click()
            print("Berjaya menekan butang Sign In")
        except Exception as e:
            print(f"Gagal tekan butang Sign In: {repr(e)}")

        time.sleep(3) 

        driver.get(url_checkin)

        # Tetapkan zoom selepas halaman mula dimuatkan
        driver.execute_script(
            "document.body.style.zoom = '50%'"
        )
        #tekan butang checkin
        try:
            wait = WebDriverWait(driver, 10)
            butangcheckin = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.checkin-button"))
            )
            if "disabled" in butangcheckin.get_attribute("class") or butangcheckin.get_attribute("disabled"):
                print(f"Sudah checkin")
                driver.get(url_trade)
            else:
                print(f"Boleh checkin")
                butangcheckin.click()
                print(f"Butang sudah ditekan")
        except Exception as e:
            print(f"{e}")
        #tekan cliam reward
        try:
            wait = WebDriverWait(driver, 10)
            claim_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.confirm-btn-primary")
                )
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", claim_btn)
            time.sleep(0.5)
            claim_btn.click()
            print("Butang claim reward ditekan")
            time.sleep(1)
        except Exception as e:
            print(f"Gagal tekan clain reward")
        driver.get(url_trade)
        # Tetapkan zoom selepas halaman mula dimuatkan
        driver.execute_script(
            "document.body.style.zoom = '50%'"
        )
        time.sleep(2)
        try:
            wait_trade = WebDriverWait(driver, 10)
            percubaan_maksimum = 5
            berjaya = False
            for percubaan in range(1, percubaan_maksimum + 1):
                print(f"Percubaan {percubaan}/{percubaan_maksimum}")
                #tekan butang max
                try:
                    butang_max = wait_trade.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.percentage-btn.max"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", butang_max)
                    time.sleep(0.5)
                    butang_max.click()
                    print("Butang max ditekan")
                    time.sleep(1)
                except Exception as e:
                    print(f"Gagal tekan max: {repr(e)}")
                    time.sleep(1)
                    continue
                #tekan butang Buy BYC
                try:
                    butang_buy = wait_trade.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-btn.buy"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", butang_buy)
                    time.sleep(0.5)
                    butang_buy.click()
                    print(f"Butang BTC ditekan")
                    berjaya = True
                    break
                except Exception as e:
                    print(f"Butang buy BTC belum sedia")
                    time.sleep(1)
                    continue
            if not berjaya:
                print(f"Gagal selepas {percubaan_maksimum} kali percubaan.")
        except Exception as e:
            print(f"Gagal tekan max dan trade: {repr(e)}")
        time.sleep(11)
        # Tunggu & tekan butang tutup (X)
        try:
            wait_close = WebDriverWait(driver, 10)
            butang_tutup = wait_close.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.close-btn"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", butang_tutup)
            time.sleep(0.5)
            butang_tutup.click()
            print("[OK] Butang tutup (X) ditekan")
            time.sleep(1)
        except Exception as e:
            print(f"[AMARAN] Gagal tekan butang tutup: {repr(e)}")
        time.sleep(2)
        driver.get(url_logout)
        time.sleep(2)
        # Tetapkan zoom selepas halaman mula dimuatkan
        driver.execute_script(
            "document.body.style.zoom = '50%'"
        )
        updateruntrade(id_input)
        # Tekan butang Logout
        try:
            logout_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, 'button.logout-btn[onclick*="confirmLogout"]')
                )
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", logout_btn)
            time.sleep(0.5)
            logout_btn.click()
            print("Berjaya menekan butang Logout")
            time.sleep(1)
        except Exception as e:
            print(f"Gagal tekan butang Logout: {repr(e)}")
        # === 10. TUNGGU & KLIK BUTANG OK ===
        try:
            # Tunggu mesej "Transfer Successful!" & butang OK
            ok_btn = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, '//button[normalize-space(text())="OK"]')
                )
            )
            time.sleep(0.5)
            ok_btn.click()
            print("Pemindahan Berjaya! Butang OK ditekan.")
            time.sleep(1)
        except Exception as e:
            print(f"Gagal tekan butang OK: {repr(e)}")
        time.sleep(2)
        driver.quit()
    except Exception as e:
        print("Ralat:", repr(e))

    finally:
        if driver is not None:
            try:
                driver.quit()
            except OSError as e:
                print("Amaran semasa menutup Chrome:", e)

        if cursor is not None:
            cursor.close()

        if db is not None and db.is_connected():
            db.close()


if __name__ == "__main__":
    main()
