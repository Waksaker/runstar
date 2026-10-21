
import undetected_chromedriver as uc
import time
import mysql.connector
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

def connect_database():
    host = "localhost"
    user = "root"
    password = ""
    database = "webpy"
    return mysql.connector.connect(host=host, user=user, password=password, database=database)


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

        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = uc.Chrome(options=options, version_main=155)
        driver.get(url_index)

        time.sleep(8)

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
            print("✅ Berjaya mengklik butang MY/EN English")
            time.sleep(1)
        except Exception as e:
            print(f"⚠️ Gagal mengklik butang: {repr(e)}")
        # === TAMAT BAHAGIAN KLIK ===

        # === 2. ISI NAMA PENGGUNA ===
        try:
            wait = WebDriverWait(driver, 15)
            username_field = wait.until(
                EC.presence_of_element_located((By.ID, "loginUser"))
            )
            username_field.clear()
            username_field.send_keys(username_input)
            print(f"✅ Nama pengguna dimasukkan: {username_input}")
        except Exception as e:
            print(f"⚠️ Gagal isi nama pengguna: {repr(e)}")

        # === 3. ISI KATA LALUAN ===
        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.ID, "loginPass"))
            )
            password_field.clear()
            password_field.send_keys(password_input)
            print("✅ Kata laluan dimasukkan")
        except Exception as e:
            print(f"⚠️ Gagal isi kata laluan: {repr(e)}")

        # === 4. KLIK BUTANG SIGN IN ===
        try:
            signin_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "loginSubmitBtn"))
            )
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", signin_btn)
            time.sleep(0.5)
            signin_btn.click()
            print("✅ Berjaya menekan butang Sign In")
        except Exception as e:
            print(f"⚠️ Gagal tekan butang Sign In: {repr(e)}")

        time.sleep(3) 

        driver.get(url_checkin)

        input("Tekan ENTER untuk menutup Chrome...")

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