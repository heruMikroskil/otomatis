import asyncio
from playwright.async_api import async_playwright
import pytesseract
import random as r
from PIL import Image

def getHP():
    hpAwalan = ["0852", "0822", "0853", "0857", "0813", "0822", "0823"]
    n1 = r.randint(1, 9999)
    n1 = f"{n1:04d}"
    n2 = r.randint(1, 9999)
    n2 = f"{n2:04d}"
    noHP = hpAwalan[r.randint(0,6)] + n1 + n2
    return noHP

async def main(nama, email, c):
    async with async_playwright() as p:
        #nama = "Player_" + str(n)
        #email = "Thu." + nama + "@gmail.com"
        noHP = getHP()
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 720, 'height': 1280})

        # 1. Buka halaman website
        print("Membuka halaman website...")
        await page.goto("https://virtual-expo.lkpp.go.id/visitor/register")
        #await page.screenshot(path="01_halaman_awal.png")
        # 2. Isi data berdasarkan ID elemen (#id_elemen)
        # Ganti 'username_input' dan 'password_input' dengan ID asli di website
        print("Mengisi formulir...")
        # await page.fill("#Nama", "user_anda")
        # await page.fill("#Email", "email_anda")
        await page.fill("#profile_name", nama)
        await page.fill("#profile_email", email)
        await page.fill("#profile_company_name", "Kementerian Imigrasi dan Pemasyarakatan")
        await page.fill("#profile_occupation", "Ditjen Imigrasi dan Pemasyarakatan")
        await page.fill("#profile_phone_number", noHP)
        await page.fill("#profile_password", "Admin123")
        await page.fill("#profile_password_confirmation", "Admin123")
        await page.check("input.form-check-input")
        #await page.screenshot(path="02_halaman_awal.png")

        # 3. Klik tombol/bagian tertentu (berdasarkan ID atau teks)
        # Contoh klik elemen dengan ID '#submit-btn'
        print("Mengeklik tombol submit...")
        await page.click("button[type='submit']")

        # Tunggu proses pemuatan setelah klik (opsional)
        await page.wait_for_timeout(5000)
        #await page.screenshot(path="03.png")
        await asyncio.sleep(3) # Tunggu elemen/canvas termuat sempurna

        # Panggil fungsi klik berdasarkan teks di dalam gambar/canvas
        #await click_text_on_image(page, "Lewati")
        
        await page.mouse.click(360, 1008)
        await page.wait_for_timeout(2000)
        
       
        #await page.screenshot(path="04.png")
        print("Lewati Selesai")
        #Close banner
        await page.mouse.click(593, 530)
        await page.wait_for_timeout(2000)
        print("Close banner selesai")

        #Klik Mengerti cookies
        await page.mouse.click(620, 1236)
        await page.wait_for_timeout(3000)
        #Masukk Hall
        await page.mouse.click(277, 654)
        await page.wait_for_timeout(2000)
        #await page.screenshot(path="05.png")
        print("Masuk Hall selesai")
        

        #Filter booth
        await page.mouse.click(420, 30)
        await page.wait_for_timeout(1000)
        #await page.screenshot(path="07.png")
        
        await page.keyboard.type("UKPBJ KEMENTERIAN IM")
        await page.wait_for_timeout(1000)
        #await page.screenshot(path="08.png")
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(2000)
        #await page.screenshot(path="09.png")

        #Whatsapp
        await page.mouse.click(370, 770)
        await page.wait_for_timeout(2000)
        namaGambar = f"{c:03d}.png"
        await page.screenshot(path=namaGambar)

        #Live chat
        await page.mouse.click(360, 669)
        await page.wait_for_timeout(2000)
        #await page.screenshot(path="11.png")
        #await page.screenshot(path="12.png")

        #aktif chat
        #await page.wait_for_timeout(3000)
        #await page.mouse.click(512, 1230)
        #await page.wait_for_timeout(1000)
        #await page.screenshot(path="13.png")
        
        #Ketik pesan
        #await page.wait_for_timeout(5000)
        #await page.keyboard.type("Halo admin")
        #await page.screenshot(path="14.png")
        #await page.wait_for_timeout(1000)
        #await page.keyboard.press("Enter")
        #await page.wait_for_timeout(3000)
        #await page.screenshot(path="15.png")
        await browser.close()

if __name__ == "__main__":
    contacts = [
    {
        "nama": "IRWAN PURNAMA",
        "email": "irwan.purnama@kemenimipas.go.id"
    },
    {
        "nama": "FATIKA SINTAWATI",
        "email": "12.fatika.sintawati.xxiv@gmail.com"
    },
    {
        "nama": "ARICO GINTING",
        "email": "19.arico.ginting.xxiv@gmail.com"
    },
    {
        "nama": "AURA ZAHRA PUTERI SUHENDI",
        "email": "22.aurazahraputerisuhendi.xxiv@gmail.com"
    },
    {
        "nama": "A.A. AGUS HERYANTO",
        "email": "a.a.agus.heryanto95@kemenimipas.go.id"
    }
    ]
    c=0
    for contact in contacts:
        nama = contact["nama"]
        email = contact["email"]
        c+=1
        #print(f"Proses: {nama} ({email})")
        asyncio.run(main(nama, email, c))
