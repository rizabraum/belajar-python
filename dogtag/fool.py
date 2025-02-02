# Date: 03-02-2024 (DD-MM-YYYY)

# Program buka dan tutup pintu berdasarkan input user

nama = str(input("\nSiapakah anda? " ))
nama = nama.title()

perintah = str(input("Masukkan perintah (Open/Close): " ))
perintah = perintah.lower()

if perintah == ("open"):
    print(f"Pintu berhasil dibuka, Hallo {nama} silahkan masuk...\n")
elif perintah == ("close"):
    print(f"Yah sayang sekali {nama}, saya kira anda ingin masuk...\n")
else: 
    print(f"Maaf {nama}, input anda tidak valid\n")