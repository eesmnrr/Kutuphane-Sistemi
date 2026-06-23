import json
from kitap import Kitap
from uye import Uye

class Kutuphane:
    def __init__(self):
        self.kitaplar = [] # Kitapların tutulacagı liste
        self.uyeler = [] # Uyelerin tutulacagı liste
        self.yukle() # Kayitli verileri yukleyip fonksiyonları calıstırır

    def kitap_ekle(self, kitap_id, ad, yazar):
        kitap = Kitap(kitap_id, ad, yazar)
        self.kitaplar.append(kitap)

    def uye_ekle(self, uye_id, ad):
        uye = Uye(uye_id, ad)
        self.uyeler.append(uye)

    def kutuphane_sifirla(self):
        self.kitaplar = []
        self.uyeler = []
        self.kaydet()  # Listeler bosaltildiktan sonra JSON dosyasini da guncelleyerek sifirlar.

    def kaydet(self):
        veriler = [] # JSON dosyasina yazilacaklari toplamak icin bos liste
        for kitap in self.kitaplar:
            # Her kitabin bilgisini sozluk ({}) yapisina cevirip listeye ekler
            veriler.append({
                "kitap_id": kitap.kitap_id,
                "ad": kitap.ad,
                "yazar": kitap.yazar,
                "oduncte": kitap.oduncte
            })
        with open("veri.json", "w", encoding="utf-8") as dosya:  # veri.json dosyasini yazma modunda ve Turkce karakter destegiyle acar
            json.dump(veriler, dosya, ensure_ascii=False, indent=4)  # Olusturulan listeyi duzenli ve Turkce olarak kaydeder

    def yukle(self):
        try:
            with open("veri.json", "r", encoding="utf-8") as dosya: # veri.json dosyasini okuma modunda acar
                veriler = json.load(dosya) # Dosyadaki verileri listeye yukler
                for veri in veriler:
                    kitap = Kitap(veri["kitap_id"], veri["ad"], veri["yazar"])
                    kitap.oduncte = veri["oduncte"]
                    self.kitaplar.append(kitap)
        except (FileNotFoundError, json.JSONDecodeError): # Dosya yoksa veya bozuksa program cokmesin diye listeyi bos baslatir
            self.kitaplar = []