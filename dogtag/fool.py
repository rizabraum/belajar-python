# Date: 03-02-2024 (DD-MM-YYYY)

# Program buka dan tutup pintu berdasarkan input user

perintah = str(input("\nMasukkan perintah (Open/Close): " ))
perintah = perintah.lower()

if perintah == ("open"):
    print("Pintu berhasil dibuka, silahkan masuk...\n")
elif perintah == ("close"):
    print("Yah sayang sekali, saya kira anda ingin masuk...\n")
else: print("input tidak valid\n")