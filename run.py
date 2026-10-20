from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Buka Google Chrome
driver = webdriver.Chrome()

# Buka website
driver.get("https://www.google.com")

# Maksimumkan tetingkap Chrome
driver.maximize_window()

# Tunggu sehingga halaman dimuatkan
wait = WebDriverWait(driver, 15)

# Paparkan tajuk website
print("Tajuk website:", driver.title)

# Cari kotak carian Google
search_box = wait.until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Masukkan teks carian
search_box.send_keys("Belajar Python Selenium")

# Tekan Enter
search_box.submit()

input("Tekan Enter untuk menutup Chrome...")

# Tutup Chrome
driver.quit()
