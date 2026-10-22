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

def updateruntransfer(id_input):
    db = None
    cursor = None
    try:
        db = connect_database()
        cursor = db.cursor()
        update_query = "UPDATE pengguna SET runtrans = '0' WHERE id = %s"
        cursor.execute(update_query, (id_input,))
        db.commit()
        print(f"Status untuk ID {id_input} telah dikemaskini kepada 'completed'.")
    except Exception as e:
        print(f"Ralat semasa mengemaskini status: {repr(e)}")
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None and db.is_connected():
            db.close()

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
        url_logout = f"{link}/settings.php"

        options = uc.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = uc.Chrome(
            options=options,
            version_main=155,
            suppress_welcome=True,
            headless=False
        )

        driver.get(url_index)

        time.sleep(2)

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

        try:
            amount_element = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'div#portfolioBalance.portfolio-amount')
                )
            )
            amount_text = amount_element.text.strip()
            print("=" * 40)
            print(f"💰 Jumlah Available Profit & Commission: {amount_text} USD")
            print("=" * 40)
            # Tukar ke nombor
            bersih = amount_text.replace("$", "").replace("USD", "").strip()
            bersih = bersih.replace(",", ".")
            jumlah_nilai = float(bersih)
            if jumlah_nilai >= 1.00:
                print("✅ Jumlah melebihi 1,00 USD. Teruskan proses.")
                # === 6. KLIK KAD PROFIT COMMISSION ===
                try:
                    profit_card = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'div.balance-card.profit')
                        )
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", profit_card)
                    time.sleep(0.5)
                    profit_card.click()
                    print("✅ Berjaya mengklik kad Profit Commission")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal mengklik kad Profit Commission: {repr(e)}")

                # === 7. KLIK trading balance ===
                try:
                    trading_option = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'div.destination-option[onclick*="trading"]')
                        )
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", trading_option)
                    time.sleep(0.5)
                    trading_option.click()
                    print("✅ Berjaya memilih Trading Balance")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal memilih Trading Balance: {repr(e)}")

                # === 8. KLIK BUTANG MAX ===
                try:
                    max_btn = wait.until(
                        EC.element_to_be_clickable(
                            (By.CSS_SELECTOR, 'span.max-amount[onclick*="setMaxAmount"]')
                        )
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", max_btn)
                    time.sleep(0.5)
                    max_btn.click()
                    print("✅ Berjaya menekan butang Max — jumlah penuh diisi")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal tekan butang Max: {repr(e)}")

                # === 9. KLIK CONFIRM TRANSFER ===
                try:
                    # Guna ID terus — paling tepat dari kod laman anda
                    confirm_btn = wait.until(
                        EC.element_to_be_clickable((By.ID, "confirmTransferBtn"))
                    )
                    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_btn)
                    time.sleep(0.5)
                    confirm_btn.click()
                    print("✅ ✅ Berjaya menekan Confirm Transfer!")
                    updateruntransfer(id_input)
                    print("🔄 Pemindahan sedang diproses...")
                    time.sleep(3)
                except Exception as e:
                    print(f"⚠️ Gagal tekan Confirm Transfer: {repr(e)}")

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
                    print("✅ ✅ Pemindahan Berjaya! Butang OK ditekan.")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal tekan butang OK: {repr(e)}")

                driver.get(url_logout)

                time.sleep(2)
                
                # Tetapkan zoom selepas halaman mula dimuatkan
                driver.execute_script(
                    "document.body.style.zoom = '50%'"
                )

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
                    print("✅ Berjaya menekan butang Logout")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal tekan butang Logout: {repr(e)}")

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
                    print("✅ ✅ Pemindahan Berjaya! Butang OK ditekan.")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal tekan butang OK: {repr(e)}")

                time.sleep(2)

                driver.quit()
            else:
                print("❌ Jumlah kurang daripada 1,00 USD. Proses dihentikan.")
                driver.get(url_logout)
                
                time.sleep(2)
                
                # Tetapkan zoom selepas halaman mula dimuatkan
                driver.execute_script(
                    "document.body.style.zoom = '50%'"
                )

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
                    print("✅ Berjaya menekan butang Logout")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal tekan butang Logout: {repr(e)}")

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
                    print("✅ ✅ Pemindahan Berjaya! Butang OK ditekan.")
                    time.sleep(1)
                except Exception as e:
                    print(f"⚠️ Gagal tekan butang OK: {repr(e)}")

                time.sleep(2)

                driver.quit()

        except Exception as e:
            print(f"⚠️ Gagal tarik jumlah: {repr(e)}")
            # Cuba pemilih alternatif jika yang atas tak berfungsi
            try:
                amount_element = driver.find_element(By.CSS_SELECTOR, '.portfolio-amount-container .portfolio-amount')
                amount_text = amount_element.text.strip()
                print("=" * 40)
                print(f"💰 Jumlah (cara ke-2): {amount_text} USD")
                print("=" * 40)
            except Exception as e2:
                print(f"❌ Cara ke-2 juga gagal: {repr(e2)}")

        # input("Tekan ENTER untuk menutup Chrome...")

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