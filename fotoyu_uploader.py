import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from selenium.webdriver.common.keys import Keys

# --- Konfigurasi ---
FOTOYU_LOGIN_URL = "https://www.fotoyu.com/login?next=%252Fprofile%252F%2520"
FOTOYU_HOME_URL = "https://www.fotoyu.com/"

# --- MASUKKAN KREDENSIAL LOGIN ANDA DI SINI ---
USERNAME = "username_kamu"
PASSWORD = "password_kamu"
# -----------------------------------------------

FOLDER_FOTO = r"E:\ALBUM FOTO\iloveimg-compressed" # Ganti sesuai lokasi fotomu

# --- Inisialisasi WebDriver ---
def setup_driver():
    print("Membuka browser Chrome...")
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Biarkan dalam komentar untuk debugging
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver
    except Exception as e:
        print(f"Error saat inisialisasi driver: {e}")
        print("Pastikan chromedriver.exe ada di PATH sistem Anda dan versinya cocok dengan Chrome.")
        exit()

# --- Fungsi Login (Tidak Berubah - Anda mengatakan ini sudah berhasil) ---
def login(driver):
    print(f"Menuju halaman login: {FOTOYU_LOGIN_URL}")
    driver.get(FOTOYU_LOGIN_URL)
    wait = WebDriverWait(driver, 30) 

    try:
        # 1. Masukkan Username/Email
        print("Mencari form username/email...")
        username_field_xpath = "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/form/div/div/div/div[2]/div[2]/div[2]/div/input"
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, username_field_xpath)))
        username_field.send_keys(USERNAME)
        print("Username/Email berhasil dimasukkan.")
        time.sleep(1)

        # Tekan ENTER setelah mengisi username/email
        username_field.send_keys(Keys.ENTER)
        print("Menekan ENTER setelah username/email.")
        time.sleep(3) 

        # 2. Masukkan Password
        print("Mencari form password...")
        password_field_xpath = "/html/body/div[1]/div/div[2]/div/div[2]/div[1]/form/div/div/div/div[2]/div[3]/div[2]/div/input"
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, password_field_xpath)))
        password_field.send_keys(PASSWORD)
        print("Password berhasil dimasukkan.")
        time.sleep(1)

        # Tekan ENTER setelah mengisi password
        password_field.send_keys(Keys.ENTER)
        print("Menekan ENTER setelah password.")
        
        # --- Strategi Muat Ulang Halaman Utama Setelah Login ---
        print("Memberi waktu setelah login dan memeriksa URL...")
        time.sleep(5) 

        current_url = driver.current_url
        print(f"URL saat ini setelah penekanan ENTER terakhir: {current_url}")

        if current_url.startswith("data:") or FOTOYU_HOME_URL not in current_url:
            print(f"URL tidak sesuai harapan ({FOTOYU_HOME_URL}) atau masih 'data:,', mencoba mengarahkan paksa ke halaman utama.")
            try:
                driver.get(FOTOYU_HOME_URL)
                print("Berhasil mengarahkan paksa ke halaman utama.")
            except WebDriverException as e:
                print(f"Kesalahan WebDriver saat mengarahkan paksa: {e}")
                return False
            time.sleep(3) 

        # Sekarang, tunggu elemen "Akun Saya" sebagai indikator sukses login
        akun_saya_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[3]"
        print(f"Menunggu elemen 'Akun Saya' ({akun_saya_xpath}) muncul di halaman...")
        wait.until(EC.element_to_be_clickable((By.XPATH, akun_saya_xpath)))
        
        print("Login berhasil! Elemen 'Akun Saya' terdeteksi di halaman beranda.")
        return True

    except TimeoutException:
        print("Gagal login: Halaman login tidak merespons, kredensial salah, atau elemen 'Akun Saya' tidak muncul.")
        print(f"URL terakhir yang terdeteksi: {driver.current_url}")
        print("Pastikan XPath benar, kredensial akurat, dan tidak ada Captcha/verifikasi tambahan.")
        return False
    except NoSuchElementException as e:
        print(f"Elemen login tidak ditemukan: {e}")
        print("XPath untuk elemen login atau 'Akun Saya' mungkin sudah berubah. Silakan periksa kembali.")
        return False
    except Exception as e:
        print(f"Terjadi kesalahan tak terduga saat login: {e}")
        return False

# --- Fungsi Unggah Foto (Revisi KRUSIAL di sini: Target Input File) ---
def upload_photo(driver, photo_path):
    wait = WebDriverWait(driver, 20)
    print("\n--- Memulai Proses Unggah Foto ---")

    try:
        # 3. Klik "Akun Saya"
        print("Mencari dan mengklik 'Akun Saya'...")
        akun_saya_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[3]"
        akun_saya_button = wait.until(EC.element_to_be_clickable((By.XPATH, akun_saya_xpath)))
        akun_saya_button.click()
        print("Berhasil mengklik 'Akun Saya'.")
        time.sleep(2)

        # 4. Klik "Unggah" (yang memunculkan popup "Pilih Tipe Konten")
        print("Mencari dan mengklik 'Unggah'...")
        unggah_xpath = "/html/body/div[1]/div/div[2]/div/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[2]"
        unggah_button = wait.until(EC.element_to_be_clickable((By.XPATH, unggah_xpath)))
        unggah_button.click()
        print("Berhasil mengklik 'Unggah'.")
        time.sleep(3) # Beri waktu lebih untuk popup "Pilih Tipe Konten" muncul sepenuhnya

        # 5. Klik "Postingan" di dalam popup "Pilih Tipe Konten"
        postingan_button_xpath = "//div[contains(@class, 'TemplateProfileUploadModal__StyledItemContainer') and .//p[text()='Postingan']]"
        print(f"Mencari dan mengklik 'Postingan' di popup dengan XPath yang lebih andal: {postingan_button_xpath}")
        postingan_button = wait.until(EC.element_to_be_clickable((By.XPATH, postingan_button_xpath)))
        postingan_button.click()
        print("Berhasil mengklik 'Postingan'.")
        time.sleep(1) # Jeda singkat setelah klik "Postingan" untuk persiapan DOM

        # --- PERBAIKAN KRUSIAL: Menargetkan input type="file" yang tepat ---
        # Menggunakan selektor class yang Anda berikan
        input_file_selector = "input.TemplateProfileTabPost__StyledUploadInput-sc-1bcab6d-4.YVUcC"
        print(f"Menemukan dan mengirimkan jalur file ke input type='file' dengan CSS Selector: {input_file_selector}")
        
        # Menggunakan CSS Selector yang spesifik
        file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_file_selector)))
        
        file_input.send_keys(photo_path)
        print("Jalur file berhasil dikirimkan. Menunggu proses upload dimulai...")
        time.sleep(5) 

        # 6. Klik tanda centang (konfirmasi unggah)
        print("Mencari dan mengklik tanda centang (konfirmasi)...")
        centang_xpath = "/html/body/div[1]/div/div[2]/div/div[2]/div/div[2]/div"
        centang_button = wait.until(EC.element_to_be_clickable((By.XPATH, centang_xpath)))
        centang_button.click()
        print("Berhasil mengklik tanda centang. Unggahan selesai.")
        time.sleep(5)

        return True

    except TimeoutException:
        print("Timeout: Salah satu elemen tidak ditemukan atau tidak merespons saat unggah.")
        print("Pastikan XPath/CSS Selector benar dan elemen-elemen muncul sesuai harapan.")
        print(f"URL saat ini: {driver.current_url}")
        return False
    except NoSuchElementException as e:
        print(f"Elemen tidak ditemukan saat unggah: {e}")
        print("XPath/CSS Selector mungkin sudah berubah atau elemen tidak ada.")
        print(f"URL saat ini: {driver.current_url}")
        return False
    except Exception as e:
        print(f"Terjadi kesalahan saat mengunggah foto: {e}")
        print(f"URL saat ini: {driver.current_url}")
        return False

# --- Main Program (Tidak Berubah) ---
if __name__ == "__main__":
    driver = setup_driver()
    if not driver:
        print("Program dihentikan karena gagal menginisialisasi driver.")
        exit()

    if USERNAME == "masukkan_username_atau_email_anda_di_sini" or PASSWORD == "masukkan_password_anda_di_ini":
        print("\n[PERINGATAN] Mohon masukkan USERNAME dan PASSWORD Anda di bagian 'Konfigurasi' dalam script!")
        driver.quit()
        exit()

    if not login(driver):
        print("Program dihentikan karena gagal login.")
        driver.quit()
        exit()

    photo_files = []
    if os.path.exists(FOLDER_FOTO) and os.path.isdir(FOLDER_FOTO):
        for filename in os.listdir(FOLDER_FOTO):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                photo_files.append(os.path.join(FOLDER_FOTO, filename))
        if not photo_files:
            print(f"Tidak ada file gambar ditemukan di folder: {FOLDER_FOTO}")
            driver.quit()
            exit()
    else:
        print(f"Folder '{FOLDER_FOTO}' tidak ditemukan atau bukan direktori yang valid.")
        driver.quit()
        exit()

    print(f"\nDitemukan {len(photo_files)} gambar untuk diunggah.")

    uploaded_count = 0
    for i, photo_path in enumerate(photo_files):
        print(f"\n--- Mengunggah foto ke-{i+1} dari {len(photo_files)}: {os.path.basename(photo_path)} ---")
        if upload_photo(driver, photo_path):
            uploaded_count += 1
            print(f"Foto '{os.path.basename(photo_path)}' berhasil diunggah.")
        else:
            print(f"Gagal mengunggah foto '{os.path.basename(photo_path)}'. Melanjutkan ke foto berikutnya.")
            print("Kembali ke halaman beranda untuk mencoba unggahan berikutnya.")
            driver.get(FOTOYU_HOME_URL)
            time.sleep(3)

    print(f"\n--- Proses Unggah Selesai ---")
    print(f"Total {uploaded_count} foto berhasil diunggah dari {len(photo_files)}.")

    driver.quit()
    print("Browser ditutup.")
