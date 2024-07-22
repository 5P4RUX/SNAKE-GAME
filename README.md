Bu proje, klasik yılan oyununu Python ve Tkinter kullanarak oluşturan bir uygulamadır. Oyuncular, yılanın hareketini kontrol ederek yemeği yemeye çalışırlar. Oyun boyunca yılan büyür ve belirli zorluk seviyelerinde daha hızlı hareket eder.

**Özellikler**
• Renkli ve modern kullanıcı arayüzü: Arka plan, yılan ve yemek için çekici renkler kullanılmıştır.
• Farklı zorluk seviyeleri: Çok Kolay'dan Çok Zor'a kadar çeşitli hız seçenekleri.
• Yüksek Skor Takibi: Oyunun en yüksek skorunu saklar ve gösterir.
• Oyun Bitti Ekranı: Oyun bittiğinde skor ve tekrar oynama seçeneği gösterir.

**Gereksinimler**

• Python 3.xtkinter modülü (Python'un standart kütüphanesi içinde gelir)random modülü (Python'un standart kütüphanesi içinde gelir)

**Kurulum**
• Proje dosyasını klonlayın veya indirin:

`git clone https://github.com/Sparux-666/SNAKE-GAME.git`
`cd SNAKE-GAME`

Termux, macOS ve Kali Linux için Kurulumu için Aşağıdaki adımları kullanarak oyunu çalıştırabilirsiniz.

**Termux**
Python'u yükleyin: pkg install pythonTkinter'i yükleyin:Termux'ta tkinter'ı doğrudan yüklemek mümkün değildir. Bu yüzden `termux-x11` kullanarak GUI uygulamalarını çalıştırmanız gerekebilir.
`pkg install termux-x11` Proje klasörüne gidin ve oyunu çalıştırın:
`cd SNAKE-GAME`
`python SnakeGame666.py`

**macOS**

Python'u ve tkinter'ı yükleyin:macOS genellikle Python ve tkinter ile birlikte gelir. Ancak, Python'un en son sürümünü yüklemek için Homebrew kullanabilirsiniz: 
`brew install python` Proje klasörüne gidin ve oyunu çalıştırın: `cd SNAKE-GAME`
`python3 SnakeGame666.py`

**Kali Linux**

Python'u ve tkinter'ı yükleyin:
`sudo apt update`
`sudo apt install python3` python3-tkProje klasörüne gidin ve oyunu çalıştırın: `cd SNAKE-GAME`
`python3 SnakeGame666.py`

**Kullanım**

Oyunu başlatın: Zorluk seviyesini seçerek oyunu başlatabilirsiniz.
Yılanı kontrol edin: Klavye yön tuşları veya ekrandaki butonlar ile yılanın yönünü değiştirin.
Yemeği yiyin: Yemeği yiyerek skoru artırın ve yılanı büyütün.
Oyunu bitirin: Yılanın kendi gövdesine çarpmasıyla oyun biter. 
Sonrasında "Tekrar Oyna" butonuyla oyunu yeniden başlatabilirsiniz.

Katkıda bulunmak için lütfen bir fork oluşturun, kendi branch'inizde geliştirme yapın ve ardından bir pull request gönderin. Projeyi fork'layın Kendi branch'inizi oluşturun.

**Lisans**
Bu proje MIT lisansı altında lisanslanmıştır - detaylar için LICENSE dosyasına bakın.
