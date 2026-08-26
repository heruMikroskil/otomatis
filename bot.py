import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Buka browser headless (tanpa tampilan visual di server)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # 1. Buka halaman website
        print("Membuka halaman website...")
        await page.goto("https://virtual-expo.lkpp.go.id/visitor/register")

        # 2. Isi data berdasarkan ID elemen (#id_elemen)
        # Ganti 'username_input' dan 'password_input' dengan ID asli di website
        print("Mengisi formulir...")
        # await page.fill("#Nama", "user_anda")
        # await page.fill("#Email", "email_anda")
        await page.fill("#profile_name", "Nama Anda")
        await page.fill("#profile_email", "Nama Anda")
        await page.fill("#profile_company_name", "Nama Anda")
        await page.fill("#profile_occupation", "Nama Anda")
        await page.fill("#profile_name", "Nama Anda")
        await page.fill("#profile_phone_number", "Nama Anda")
        await page.fill("#profile_password", "Nama Anda")
        await page.fill("#profile_password_confirmation", "Nama Anda")
        await page.check("input.form-check-input")


        # 3. Klik tombol/bagian tertentu (berdasarkan ID atau teks)
        # Contoh klik elemen dengan ID '#submit-btn'
        print("Mengeklik tombol submit...")
        await page.click("button[type='submit']")

        # Tunggu proses pemuatan setelah klik (opsional)
        await page.wait_for_timeout(5000)

        print("Proses otomatis selesai!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())