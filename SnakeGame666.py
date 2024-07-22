import tkinter as tk
import random

# Sabitler
OYUN_BOYUTU = 600  # Oyun alanı boyutu (genişlik ve yükseklik)
KARE_BOYUTU = 20  # Her bir kare boyutu
GOVDE_PARCALARI = 3
YILAN_RENGI = "#FF69B4"  # Pembe renk
YEMEK_RENGI = "#DA70D6"  # Mor renk
ARKA_PLAN_RENGI = "#1c0f45"  # Arka plan rengi
IZGARA_RENGI = "#FFC0CB"  # Açık pembe
MAX_SKOR = 99
YAZI_TIPI = ("Arial Narrow", 12)
OYUN_BITTI_YAZI_TIPI = ("Arial Narrow", 14, "bold")

# Zorluk ayarları
ZORLUK_AYARLARI = {
    'Çok Kolay': 200,
    'Kolay': 175,
    'Orta': 150,
    'Zor': 125,
    'Çok Zor': 100
}

def oyunu_baslat(zorluk):
    global HIZ
    HIZ = ZORLUK_AYARLARI[zorluk]
    zorluk_penceresi.destroy()
    ana_oyun_penceresi_goster()

def zorluk_penceresi_goster():
    global zorluk_penceresi
    zorluk_penceresi = tk.Tk()
    zorluk_penceresi.title("Zorluk Seçimi")

    tk.Label(zorluk_penceresi, text="Zorluk Seçin", font=("Arial Narrow", 24), bg=ARKA_PLAN_RENGI, fg="#FFC0CB").pack(pady=20)

    buton_cercevesi = tk.Frame(zorluk_penceresi, bg=ARKA_PLAN_RENGI)
    buton_cercevesi.pack(pady=20)

    buton_genislik = 15
    buton_yukseklik = 2
    for zorluk in ZORLUK_AYARLARI.keys():
        buton = tk.Button(buton_cercevesi, text=zorluk, font=("Arial Narrow", 16), bg="#DA70D6", fg="white", activebackground="#BF5FFF", width=buton_genislik, height=buton_yukseklik, command=lambda d=zorluk: oyunu_baslat(d))
        buton.pack(pady=10)

    zorluk_penceresi.configure(bg=ARKA_PLAN_RENGI)
    zorluk_penceresi.geometry("300x400")
    zorluk_penceresi.resizable(False, False)
    zorluk_penceresi.mainloop()

class Yilan:
    def __init__(self):
        self.govde_boyutu = GOVDE_PARCALARI
        self.koordinatlar = [[OYUN_BOYUTU // 2, OYUN_BOYUTU // 2]]  # Ekranın ortasında başla
        self.kareler = []

        for x, y in self.koordinatlar:
            kare = canvas.create_rectangle(x, y, x + KARE_BOYUTU, y + KARE_BOYUTU, fill=YILAN_RENGI, tag="yilan")
            self.kareler.append(kare)

class Yemek:
    def __init__(self):
        self.koordinatlar = self.pozisyonu_rastgele()
        self.yemek_ciz()

    def pozisyonu_rastgele(self):
        x = random.randint(0, (OYUN_BOYUTU // KARE_BOYUTU - 1)) * KARE_BOYUTU
        y = random.randint(0, (OYUN_BOYUTU // KARE_BOYUTU - 1)) * KARE_BOYUTU
        return [x, y]

    def yemek_ciz(self):
        x, y = self.koordinatlar
        canvas.create_rectangle(x, y, x + KARE_BOYUTU, y + KARE_BOYUTU, fill=YEMEK_RENGI, tag="yemek")

def sonraki_hamle(yilan, yemek):
    global yon, skor, en_yuksek_skor

    x, y = yilan.koordinatlar[0]

    if yon == "yukari":
        y -= KARE_BOYUTU
    elif yon == "asagi":
        y += KARE_BOYUTU
    elif yon == "sol":
        x -= KARE_BOYUTU
    elif yon == "sag":
        x += KARE_BOYUTU

    # Sınırdan geçiş yapabilmek için koordinatları güncelle
    if x < 0:
        x = OYUN_BOYUTU - KARE_BOYUTU
    elif x >= OYUN_BOYUTU:
        x = 0
    elif y < 0:
        y = OYUN_BOYUTU - KARE_BOYUTU
    elif y >= OYUN_BOYUTU:
        y = 0

    yilan.koordinatlar.insert(0, [x, y])
    kare = canvas.create_rectangle(x, y, x + KARE_BOYUTU, y + KARE_BOYUTU, fill=YILAN_RENGI)
    yilan.kareler.insert(0, kare)

    if x == yemek.koordinatlar[0] and y == yemek.koordinatlar[1]:
        skor += 1
        if skor > en_yuksek_skor:
            en_yuksek_skor = skor
        etiket.config(text=f"Skor: {skor}   En Yüksek Skor: {en_yuksek_skor}")
        canvas.delete("yemek")
        yemek = Yemek()
    else:
        # Eski yılan parçasını temizle
        del yilan.koordinatlar[-1]
        canvas.delete(yilan.kareler[-1])
        del yilan.kareler[-1]

    if carpismalari_kontrol_et(yilan):
        oyun_bitti()
    else:
        pencere.after(HIZ, sonraki_hamle, yilan, yemek)

def yon_degistir(yeni_yon):
    global yon
    if yeni_yon == 'sol' and yon != 'sag':
        yon = yeni_yon
    elif yeni_yon == 'sag' and yon != 'sol':
        yon = yeni_yon
    elif yeni_yon == 'yukari' and yon != 'asagi':
        yon = yeni_yon
    elif yeni_yon == 'asagi' and yon != 'yukari':
        yon = yeni_yon

def carpismalari_kontrol_et(yilan):
    x, y = yilan.koordinatlar[0]
    if [x, y] in yilan.koordinatlar[1:]:
        return True
    return False

def oyun_bitti():
    global en_yuksek_skor
    canvas.delete(tk.ALL)
    canvas.create_text(OYUN_BOYUTU / 2, OYUN_BOYUTU / 2 - 30, font=OYUN_BITTI_YAZI_TIPI, text="OYUN BİTTİ", fill="#FF69B4", tag="oyun_bitti")  # Pembe
    canvas.create_text(OYUN_BOYUTU / 2, OYUN_BOYUTU / 2 + 30, font=YAZI_TIPI, text=f"Son Skor: {skor}", fill="white", tag="oyun_bitti")
    tekrar_oyna_butonu.pack(pady=20)  # Tekrar oyna butonunu göster

def oyunu_sifirla():
    global skor, yon, yilan, yemek
    canvas.delete(tk.ALL)
    grid_ciz()
    skor = 0
    yon = 'asagi'
    etiket.config(text=f"Skor: {skor}   En Yüksek Skor: {en_yuksek_skor}")
    
    # Eski yılanı temizleyin
    if 'yilan' in globals():
        for kare in yilan.kareler:
            canvas.delete(kare)
    
    yilan = Yilan()
    yemek = Yemek()
    tekrar_oyna_butonu.pack_forget()  # Tekrar oyna butonunu gizle
    sonraki_hamle(yilan, yemek)

def grid_ciz():
    for x in range(0, OYUN_BOYUTU, KARE_BOYUTU):
        canvas.create_line(x, 0, x, OYUN_BOYUTU, fill=IZGARA_RENGI)
    for y in range(0, OYUN_BOYUTU, KARE_BOYUTU):
        canvas.create_line(0, y, OYUN_BOYUTU, y, fill=IZGARA_RENGI)

def ana_oyun_penceresi_goster():
    global pencere, skor, en_yuksek_skor, yon, yilan, yemek, etiket, canvas, tekrar_oyna_butonu

    pencere = tk.Tk()
    pencere.title("Yılan Oyunu")

    # Pencere boyutunu oyun ve kontrolleri kapsayacak şekilde ayarlama
    pencere_genislik = OYUN_BOYUTU
    pencere_yukseklik = OYUN_BOYUTU + 150
    pencere.geometry(f"{pencere_genislik}x{pencere_yukseklik}")
    pencere.resizable(False, False)
    pencere.configure(bg=ARKA_PLAN_RENGI)

    skor = 0
    en_yuksek_skor = 0
    yon = 'asagi'

    etiket = tk.Label(pencere, text=f"Skor: {skor}   En Yüksek Skor: {en_yuksek_skor}", font=YAZI_TIPI, fg="white", bg=ARKA_PLAN_RENGI)
    etiket.pack()

    canvas = tk.Canvas(pencere, bg=ARKA_PLAN_RENGI, height=OYUN_BOYUTU, width=OYUN_BOYUTU)
    canvas.pack()

    grid_ciz()

    tekrar_oyna_butonu = tk.Button(pencere, text="Tekrar Oyna", command=oyunu_sifirla, font=("Arial Narrow", 14), bg="#FF69B4", fg="white")  # Pembe
    tekrar_oyna_butonu.pack(pady=20)
    tekrar_oyna_butonu.pack_forget()  # Başlangıçta butonu gizle

    kontrol_cercevesi = tk.Frame(pencere, bg=ARKA_PLAN_RENGI)
    kontrol_cercevesi.pack(pady=20)

    btn_yukari = tk.Button(kontrol_cercevesi, text="▲", command=lambda: yon_degistir('yukari'), font=("Arial Narrow", 14), bg="#DA70D6", fg="white", activebackground="#BF5FFF", width=4, height=2)  # Mor
    btn_yukari.grid(row=0, column=1)

    btn_sola = tk.Button(kontrol_cercevesi, text="◄", command=lambda: yon_degistir('sol'), font=("Arial Narrow", 14), bg="#DA70D6", fg="white", activebackground="#BF5FFF", width=4, height=2)  # Mor
    btn_sola.grid(row=1, column=0)

    btn_asagi = tk.Button(kontrol_cercevesi, text="▼", command=lambda: yon_degistir('asagi'), font=("Arial Narrow", 14), bg="#DA70D6", fg="white", activebackground="#BF5FFF", width=4, height=2)  # Mor
    btn_asagi.grid(row=1, column=1)

    btn_saga = tk.Button(kontrol_cercevesi, text="►", command=lambda: yon_degistir('sag'), font=("Arial Narrow", 14), bg="#DA70D6", fg="white", activebackground="#BF5FFF", width=4, height=2)  # Mor
    btn_saga.grid(row=1, column=2)

    yilan = Yilan()
    yemek = Yemek()

    sonraki_hamle(yilan, yemek)

    pencere.mainloop()

zorluk_penceresi_goster()
