# Fotoyu Auto Uploader
![logo-fotoyu](https://github.com/user-attachments/assets/8f1e28ca-7dd0-48e3-8ddb-b87f9212af92)


[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-Webdriver-orange.svg)](https://selenium.dev/)
[![Chrome](https://img.shields.io/badge/Browser-Chrome-red.svg)](https://www.google.com/chrome/)

Fotoyu Auto Uploader adalah skrip Python yang memanfaatkan Selenium WebDriver untuk mengotomatiskan proses *login* dan mengunggah banyak foto ke platform Fotoyu. Skrip ini dirancang untuk membantu pengguna mengunggah koleksi foto mereka secara massal, menghindari keharusan mengunggah satu per satu secara manual melalui antarmuka web.

---

## Fitur Utama

* **Otomatisasi Login**: Secara otomatis *login* ke akun Fotoyu Anda menggunakan kredensial yang disediakan.
* **Unggah Foto Massal**: Unggah beberapa *file* gambar (PNG, JPG, JPEG, GIF, WEBP) dari folder lokal.
* **Penanganan Kesalahan**: Termasuk penanganan dasar untuk kegagalan *login* atau unggah, memungkinkan skrip untuk melanjutkan ke foto berikutnya jika terjadi kesalahan.

---

## Persyaratan

Sebelum menjalankan skrip ini, pastikan Anda memiliki hal-hal berikut:

* **Python 3.x** terinstal di sistem Anda.
* **Google Chrome** terinstal.
* **ChromeDriver** yang kompatibel dengan versi Chrome Anda. Pastikan `chromedriver.exe` berada di PATH sistem Anda atau di direktori yang sama dengan skrip Python.
* **Koneksi internet** yang stabil.

---

## Instalasi

1.  **Kloning repositori ini** (atau unduh *file* `fotoyu_uploader.py`):

    ```bash
    git clone https://github.com/syaibar/Fotoyu-Auto-Uploader.git
    cd Fotoyu-Auto-Uploader
    ```

2.  **Instal pustaka Python yang diperlukan**:

    ```bash
    pip install selenium
    ```

3.  **Unduh ChromeDriver**:
    Kunjungi [situs web ChromeDriver](https://chromedriver.chromium.org/downloads) dan unduh versi yang sesuai dengan versi Google Chrome Anda. Ekstrak *file* `chromedriver.exe` dan letakkan di direktori yang dapat diakses oleh PATH sistem Anda, atau letakkan langsung di folder yang sama dengan skrip `fotoyu_uploader.py`.

---

## Penggunaan

1.  **Konfigurasi Kredensial dan Lokasi Foto**:
    Buka *file* `fotoyu_uploader.py` dan ubah bagian konfigurasi berikut:

    ```python
    # --- MASUKKAN KREDENSIAL LOGIN ANDA DI SINI ---
    USERNAME = "username_kamu" # Ganti dengan username atau email Fotoyu Anda
    PASSWORD = "password_kamu" # Ganti dengan password Fotoyu Anda
    # -----------------------------------------------

    FOLDER_FOTO = r"E:\ALBUM FOTO\iloveimg-compressed" # Ganti dengan path folder tempat foto Anda berada
    ```
    **Penting**: Pastikan Anda mengganti *placeholder* `username_kamu`, `password_kamu`, dan `FOLDER_FOTO` dengan informasi yang benar.

2.  **Jalankan Skrip**:
    Buka terminal atau *command prompt*, navigasikan ke direktori tempat Anda menyimpan skrip, lalu jalankan:

    ```bash
    python fotoyu_uploader.py
    ```

3.  **Pantau Proses**:
    Skrip akan membuka *browser* Chrome, melakukan *login*, dan mulai mengunggah foto satu per satu. Anda akan melihat *output* di konsol yang menunjukkan status setiap unggahan.

---

## Pemecahan Masalah

* **"Error saat inisialisasi driver: ..."**: Ini sering berarti `chromedriver.exe` tidak ditemukan atau versinya tidak cocok dengan versi Chrome Anda. Pastikan `chromedriver.exe` ada di PATH atau di direktori skrip, dan cocokkan versinya.
* **"Gagal login: Halaman login tidak merespons, kredensial salah..."**: Periksa kembali **USERNAME** dan **PASSWORD** Anda di skrip. Pastikan tidak ada kesalahan ketik. Terkadang, situs web mungkin memiliki CAPTCHA atau langkah verifikasi tambahan yang tidak dapat diatasi oleh skrip otomatis ini.
* **"Elemen tidak ditemukan saat unggah: ..."** atau **"Timeout: Salah satu elemen tidak ditemukan..."**: Ini menunjukkan bahwa XPath atau CSS Selector yang digunakan dalam skrip mungkin sudah tidak valid karena perubahan pada tata letak situs web Fotoyu. Anda mungkin perlu memeriksa kembali elemen-elemen di situs web menggunakan alat pengembang *browser* (*Inspect Element*) dan memperbarui XPath/CSS Selector di skrip.
* **"Tidak ada file gambar ditemukan di folder..."**: Pastikan **FOLDER_FOTO** mengarah ke direktori yang benar dan berisi *file* gambar dengan ekstensi yang didukung (`.png`, `.jpg`, `.jpeg`, `.gif`, `.webp`).

---

## Kontribusi

Kontribusi disambut baik! Jika Anda menemukan *bug* atau memiliki saran untuk perbaikan, silakan buka *issue* atau buat *pull request*.

---

## Lisensi

Proyek ini dilisensikan di bawah lisensi MIT. Lihat *file* `LICENSE` untuk detail lebih lanjut.

---
