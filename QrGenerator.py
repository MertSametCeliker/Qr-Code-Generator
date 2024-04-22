import os
import qrcode
import tkinter as tk
from tkinter import filedialog

def generate_qr_code():
    url = url_entry.get()
    directory = directory_entry.get()
    filename = filename_entry.get()

    # URL'yi QR koduna dönüştür
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # QR kodunu bir görüntü dosyasına kaydet (JPEG formatında)
    filepath = os.path.join(directory, filename + ".jpg")  # Dosya uzantısını ekleyin
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filepath)

    result_label.config(text=f"{filename}.jpg adlı QR kodu oluşturuldu.")  # Sonucu güncelleyin

def browse_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

# Tkinter penceresi oluştur
window = tk.Tk()
window.title("QR Kodu Oluşturucu")

# URL Girişi
url_label = tk.Label(window, text="URL:")
url_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
url_entry = tk.Entry(window, width=40)
url_entry.grid(row=0, column=1, padx=10, pady=5, columnspan=2)

# Kaydedilecek Dizin Girişi
directory_label = tk.Label(window, text="Kaydedilecek Dizin:")
directory_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
directory_entry = tk.Entry(window, width=30)
directory_entry.grid(row=1, column=1, padx=10, pady=5)
browse_button = tk.Button(window, text="Gözat", command=browse_directory)
browse_button.grid(row=1, column=2, pady=5)

# Dosya Adı Girişi
filename_label = tk.Label(window, text="Dosya Adı:")
filename_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
filename_entry = tk.Entry(window, width=30)
filename_entry.grid(row=2, column=1, padx=10, pady=5)

# QR Kodu Oluştur Butonu
generate_button = tk.Button(window, text="QR Kodu Oluştur", command=generate_qr_code)
generate_button.grid(row=3, column=1, pady=10)

# Sonuç Etiketi
result_label = tk.Label(window, text="", fg="green")
result_label.grid(row=4, column=1, pady=5)

# Pencereyi göster
window.mainloop()
