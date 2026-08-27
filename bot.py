import asyncio
from playwright.async_api import async_playwright
import pytesseract
from PIL import Image

async def click_text_on_image(page, target_text):
    # 1. Simpan screenshot sementara untuk dianalisis
    screenshot_path = "ocr.png"
    await page.screenshot(path=screenshot_path)

    # 2. Baca gambar menggunakan Tesseract OCR untuk mendapatkan data posisi teks
    img = Image.open(screenshot_path)
    ocr_data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    found = False
    # 3. Cari kata target di dalam hasil OCR
    for i in range(len(ocr_data['text'])):
        text = ocr_data['text'][i].strip()
        if target_text.lower() in text.lower() and int(ocr_data['conf'][i]) > 30: # Tingkat akurasi > 30%
            # Hitung titik tengah koordinat (X, Y) dari teks
            x = ocr_data['left'][i] + (ocr_data['width'][i] // 2)
            y = ocr_data['top'][i] + (ocr_data['height'][i] // 2)
            
            print(f"Teks '{target_text}' ditemukan pada koordinat X:{x}, Y:{y}. Melakukan klik...")
            
            # 4. Klik koordinat layar tersebut
            await page.mouse.click(x, y)
            found = True
            break

    if not found:
        print(f"Teks '{target_text}' tidak ditemukan pada gambar/canvas.")

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 720, 'height': 1280})

        # 1. Buka halaman website
        print("Membuka halaman website...")
        await page.goto("https://virtual-expo.lkpp.go.id/visitor/register")
        await page.screenshot(path="01_halaman_awal.png")
        # 2. Isi data berdasarkan ID elemen (#id_elemen)
        # Ganti 'username_input' dan 'password_input' dengan ID asli di website
        print("Mengisi formulir...")
        # await page.fill("#Nama", "user_anda")
        # await page.fill("#Email", "email_anda")
        await page.fill("#profile_name", "Player006")
        await page.fill("#profile_email", "o.player006@gmail.com")
        await page.fill("#profile_company_name", "Indonesia")
        await page.fill("#profile_occupation", "Boss")
        await page.fill("#profile_phone_number", "082288997788")
        await page.fill("#profile_password", "Admin123")
        await page.fill("#profile_password_confirmation", "Admin123")
        await page.check("input.form-check-input")
        await page.screenshot(path="02_halaman_awal.png")

        # 3. Klik tombol/bagian tertentu (berdasarkan ID atau teks)
        # Contoh klik elemen dengan ID '#submit-btn'
        print("Mengeklik tombol submit...")
        await page.click("button[type='submit']")

        # Tunggu proses pemuatan setelah klik (opsional)
        await page.wait_for_timeout(5000)
        await page.screenshot(path="03_halaman_awal.png")
        await asyncio.sleep(3) # Tunggu elemen/canvas termuat sempurna

        # Panggil fungsi klik berdasarkan teks di dalam gambar/canvas
        await click_text_on_image(page, "Lewati")
        await page.wait_for_timeout(2000)
        await page.screenshot(path="04_halaman_awal.png")
        print("Proses otomatis selesai!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
