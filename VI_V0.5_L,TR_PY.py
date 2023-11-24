import requests
import os
import tkinter as tk
from pathlib import Path

# Global olarak tanımlanan step değişkeni
step = 0
selected_path = 'C:/Voider'  # Başlangıçta kullanılacak varsayılan path

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def create_folder_and_copy(files, folder_path):
    Path(folder_path).mkdir(parents=True, exist_ok=True)
    for file_info in files:
        download_file(file_info['url'], os.path.join(folder_path, file_info['save_path']))

def download_and_copy_to_folder():
    files_to_download = [
        {'url': 'https://github.com/murat725178252/VoiderInstaller/raw/main/Voider/Voider.py', 'save_path': 'Voider.py'},
        {'url': 'https://github.com/murat725178252/VoiderInstaller/raw/main/Voider/logo.png', 'save_path': 'logo.png'}
    ]

    create_folder_and_copy(files_to_download, selected_path)

    # İkinci pencereyi kapat
    done()
    

# Ana pencere
main_screen = tk.Tk()
main_screen.geometry("500x400")
main_screen.resizable(False, False)
main_screen.config(bg="GREY")
main_screen.title("Voider Yükleyici | TR , V0.1, VoiderV0.5")

def stepplus():
    # global anahtar kelimesi ile global değişkeni güncelle
    global step
    step += 1
    # her adımda devam butonunu göster
    continuebtn.pack()
    if step == 1:
        step1()
        print("1")
    elif step == 2:
        step2()
        print("2")
    elif step == 3:
        letsdownloand()
        print("3")

def step1():
    label1.pack()

def step2():
    label1.config(text="Bu Dizinine İndirilecektir, 1 MB den küçüktür \n Dosyayı Çalıştırmak için Python kodlama dilinin yüklü olması gerekir \n English ve türkçe dillerini destekler")

def letsdownloand():
    # download_button'ı paketleme işlemi kaldırıldı
    label1.config(text="İndirmeye Başlayın! \n  \n  ")
    download_button.pack()
    continuebtn.pack_forget()
    path_label.pack()
    path_radio1.pack()
    path_radio2.pack()
    pass

def set_selected_path(path):
    global selected_path
    selected_path = path
    path_label.config(text=f"Seçilen Path: {selected_path}")

def done():
    label1.config(text="Herşey Tamam! \n Bu Pencereyi Kapatabilirsiniz \n| NOT : Oluşturulan *VISettings.vis* Dosyasını Silmeyin ve Voider Yükleyici ile aynı dizinde olmasına dikkat edin\n Yoksa Voider Yükleyici iyi çalışamaz -Path konumuna bakamamasından reInstall, Uninstall Çalışmaz")
    path_label.pack_forget()
    path_radio1.pack_forget()
    path_radio2.pack_forget()
    download_button.pack_forget()
# Devam butonu tıklandığında step artırılır
continuebtn = tk.Button(main_screen, text="Devam -->", bg="BLACK", fg="WHITE", command=stepplus)

# İlk adımda devam butonunu göster
continuebtn.pack()

# İkinci adımda gösterilecek olan etiket
label1 = tk.Label(main_screen, bg="GREY", text="Voider İndiriciye Hoşgeldiniz! \n \n Voider Özeti: \n Proje Dosyaları Oluşturmak, ve Eğlence \n Yararlar: \n Hızlı Proje, Dosya Oluşturma vb.")


# Seçilen Path'i gösteren etiket
path_label = tk.Label(main_screen, bg="GREY", fg="WHITE", text=f"Seçilen Path: {selected_path}")

# İndirme butonu
download_button = tk.Button(main_screen, text="İndir ve Kur", command=download_and_copy_to_folder)

# "Done" butonu
done_button = tk.Button(main_screen, text="Tamamlandı", command=done)

# Path seçim radiobuttonları
path_radio_var = tk.StringVar()

path_radio1 = tk.Radiobutton(main_screen, text="C:/Voider", variable=path_radio_var, value="C:/Voider", command=lambda: set_selected_path("C:/Voider"))
# Masaüstü konumunu al
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop\Voider')
print(desktop_path)
# Daha sonra bu konumu kullanabilirsiniz
path_radio2 = tk.Radiobutton(main_screen, text="Masaüstü'ne İndir", variable=path_radio_var, value=desktop_path, command=lambda: set_selected_path(desktop_path))

# Buraya ihtiyacınıza göre daha fazla path ekleyebilirsiniz...

# Yerleştirme

# Diğer bileşenleri yerleştirin...
main_screen.mainloop()
