import tkinter as tk
from tkinter import messagebox
from kutuphane import Kutuphane

class KutuphaneArayuz:
    def __init__(self):
        self.kutuphane = Kutuphane()

    # ANA PENCERE KURULUMU
        self.pencere = tk.Tk()
        self.pencere.title("Kütüphane Yönetim Sistemi")
        self.pencere.geometry("650x450")

        self.pencere.columnconfigure(0, weight=1)
        self.pencere.columnconfigure(1, weight=2)
        self.pencere.configure(bg="#FDF6EC") # Sıcak Krem Rengi

        # Kutu ve Etiketler
        tk.Label(self.pencere, text="Kitap/Üye ID:", bg="#FDF6EC", fg="#5C4033", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.entry_id = tk.Entry(self.pencere)
        self.entry_id.grid(row=0, column=1, sticky="ew", padx=10, pady=5)

        tk.Label(self.pencere, text="Kitap/Üye Adı:", bg="#FDF6EC", fg="#5C4033", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.entry_ad = tk.Entry(self.pencere)
        self.entry_ad.grid(row=1, column=1, sticky="ew", padx=10, pady=5)

        tk.Label(self.pencere, text="Kitap Yazarı:", bg="#FDF6EC", fg="#5C4033", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.entry_yazar = tk.Entry(self.pencere)
        self.entry_yazar.grid(row=2, column=1, sticky="ew", padx=10, pady=5)

        # Renklendirme
        self.entry_id.configure(bg="#FFFFFF", fg="#5C4033", relief="flat", bd=2)
        self.entry_ad.configure(bg="#FFFFFF", fg="#5C4033", relief="flat", bd=2)
        self.entry_yazar.configure(bg="#FFFFFF", fg="#5C4033", relief="flat", bd=2)
       
    # ISLEM BUTONLARI
        
        tk.Button(
            self.pencere, text="Kitap Ekle", command=self.kitap_ekle_islem,
            bg="#8FBC8F", fg="#FFFFFF", activebackground="#719A71",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=3, column=0, sticky="ew", padx=10, pady=4)

        tk.Button(
            self.pencere, text="Üye Ekle", command=self.uye_ekle_islem,
            bg="#8FBC8F", fg="#FFFFFF", activebackground="#719A71",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=4, column=0, sticky="ew", padx=10, pady=4)

        tk.Button(
            self.pencere, text="Kitap Ödünç Ver", command=self.odunc_ver_islem,
            bg="#CD853F", fg="#FFFFFF", activebackground="#B87333",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=5, column=0, sticky="ew", padx=10, pady=4)

        tk.Button(
            self.pencere, text="Kitap İade Al", command=self.iade_al_islem,
            bg="#CD853F", fg="#FFFFFF", activebackground="#B87333",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=6, column=0, sticky="ew", padx=10, pady=4)
        
        tk.Button(
            self.pencere, text="Kitapları Göster", command=self.kitaplari_yenile,
            bg="#C19A6B", fg="#FFFFFF", activebackground="#A8845B",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=7, column=0, sticky="ew", padx=10, pady=4)

        tk.Button(
            self.pencere, text="Üyeleri Göster", command=self.uyeleri_yenile,
            bg="#C19A6B", fg="#FFFFFF", activebackground="#A8845B",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=8, column=0, sticky="ew", padx=10, pady=4)

        tk.Button(
            self.pencere, text="Kütüphaneyi Sıfırla", command=self.kutuphane_sifirla_islem, 
            bg="#E2725B", fg="#FFFFFF", activebackground="#C45E49",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=9, column=0, sticky="ew", padx=10, pady=4)

        tk.Button(
            self.pencere, text="Sistemi Kaydet ve Çık", command=self.guvenli_cikis,
            bg="#5C4033", fg="#FFFFFF", activebackground="#4A3228",
            bd=0, relief="flat", font=("Arial", 10, "bold"), cursor="hand2"
        ).grid(row=10, column=0, sticky="ew", padx=10, pady=8)
        
    # GOSTERIM ALANI (LISTBOX)
        self.listbox = tk.Listbox(self.pencere)
        self.listbox.grid(row=3, column=1, rowspan=8, sticky="nsew", padx=10, pady=5)
        
        self.listbox.configure(
            bg="#FFFDF9",                         
            fg="#5C4033",                         
            bd=0, relief="flat",
            highlightbackground="#EFE6D5",        
            highlightcolor="#CD853F",             
            font=("Segoe UI", 10),
            selectbackground="#CD853F",           
            selectforeground="#FFFFFF"            
        )

        self.kitaplari_yenile() # Program ilk acildiginda kayitli kitaplarin listede gorunmesini saglar.

    # KITAP EKLE
    def kitap_ekle_islem(self):
        try:
            kid = int(self.entry_id.get()) # Kitap ID'sini tam sayiya cevirir, harf girilirse ValueError gelir.
            ad = self.entry_ad.get().strip() # Ad alanindaki boslukları siler.
            yazar = self.entry_yazar.get().strip() # Yazar alanindaki boslukları siler.

            # Metin alanlari bossa except bloguna gonderir.
            if not ad or not yazar:
                raise ValueError("Boş Alan")

            self.kutuphane.kitap_ekle(kid, ad, yazar)
            self.kutulari_temizle()
            self.kitaplari_yenile() # Listbox'i gunceller.
            messagebox.showinfo("ÇIKTI", "Kitap başarıyla eklendi.")

        except ValueError: # Sayi/bos alan hatasinda ekrana uyari gelir.
            messagebox.showwarning("Hata", "Lütfen ID alanına sayı girin ve tüm alanları doldurun!")

    # UYE EKLE
    def uye_ekle_islem(self):
        try:
            uid = int(self.entry_id.get()) # Uye ID'sini tam sayiya cevirir, harf girilirse ValueError gelir.
            ad = self.entry_ad.get().strip() # Uye adindaki bosluklari temizler.

            # Metin alanlari bossa except bloguna gonderir.
            if not ad:
                raise ValueError("Boş Alan")

            self.kutuphane.uye_ekle(uid, ad)
            self.kutulari_temizle()
            self.uyeleri_yenile() # Listbox'i gunceller.
            messagebox.showinfo("ÇIKTI", "Üye başarıyla eklendi.")

        except ValueError: # Sayi/bos alan hatasinda ekrana uyari gelir.
            messagebox.showwarning("Hata", "Lütfen ID alanına sayı girin ve Ad alanını doldurun!")

    # KITAP ODUNC VER
    def odunc_ver_islem(self):
        try:
            kid = int(self.entry_id.get())  # Girilen kitap ID'sini alir.
            uid = int(self.entry_ad.get())  # Ödünç alacak Üye ID'sini alır.

            # Uye var mı yok mu kontrol edilir. 
            uye_bulundu = False
            for uye in self.kutuphane.uyeler:
                if uye.uye_id == uid:
                    uye_bulundu = True
                    break
            
            if not uye_bulundu:
                messagebox.showerror("Hata", f"{uid} ID'li bir üye sistemde kayıtlı değil!")
                return

            # Uye varsa odunc islemi
            for kitap in self.kutuphane.kitaplar:
                if kitap.kitap_id == kid:
                    if kitap.oduncte: # Kitap baskasindaysa uyari verir.
                        messagebox.showinfo("ÇIKTI", "Bu kitap ödünç verilmiş! (Üye ID: {kitap.uye_id})")
                    else: # Kitap raftaysa odunc verme islemini onaylar.
                        kitap.oduncte = True # Kitap durumunu 'oduncte' olarak gunceller.
                        kitap.uye_id = uid  # Kitaba üyenin ID'sini işlendi.
                        messagebox.showinfo("ÇIKTI", f"Kitap {uid} ID'li üyeye ödünç verildi.")

                        self.kutulari_temizle()  # Giriş kutularını boşaltır.
                        self.kitaplari_yenile()  # Listbox'ı günceller.
                    return

            messagebox.showerror("Hata", "Kitap bulunamadı.") # Kitap bulunamadiysa hata verir.

        except ValueError:
            messagebox.showwarning("Hata", "Ödünç vermek için ID alanına Kitap ID, Ad alanına ise Üye ID giriniz!" )
  
    
    # KITAP IADE AL
    def iade_al_islem(self):
        try:
            kid = int(self.entry_id.get()) # İade edilecek kitap ID'sini alir.
            
            for kitap in self.kutuphane.kitaplar:
                if kitap.kitap_id == kid:
                    kitap.oduncte = False # Kitabi tekrar oduncte degil konumuna getirir.
                    kitap.uye_id = None  # Kitap geri geldi, üzerindeki üye ID'si silindi.
                    messagebox.showinfo("ÇIKTI", "Kitap iade alındı.")
                    
                    self.kutulari_temizle()     # Giriş kutularını boşaltır
                    self.kitaplari_yenile()     # Listbox'ı günceller.
                    return
                
            messagebox.showerror("Hata", "Kitap bulunamadı.") # İade edilmek istenen ID'de kitap yoksa uyari verir.

        except ValueError:
            messagebox.showwarning("Hata", "Lütfen geçerli bir Kitap ID girin!")

    # LISTBOX YENİLEME
    def kitaplari_yenile(self): 
        self.listbox.delete(0, tk.END) # Listbox'in icindeki eski yazilari temizler.
        if not self.kutuphane.kitaplar: # Eger kayitli kitap yoksa
            self.listbox.insert(tk.END, "Kayıtlı kitap yok.")
            return # Fonksiyon sonlanir.
        
        for kitap in self.kutuphane.kitaplar:
            durum = f"Ödünçte (Üye ID: {kitap.uye_id})" if kitap.oduncte else "Mevcut"  # Kitabin durumuna gore yazilacak metni secer.
            satir = f"ID: {kitap.kitap_id} | {kitap.ad} - {kitap.yazar} ({durum})"
            self.listbox.insert(tk.END, satir) # Metin listeye eklenir.


    def uyeleri_yenile(self): 
        self.listbox.delete(0, tk.END) # Listbox'in icindeki eski yazilari temizler.
        if not self.kutuphane.uyeler: # Eger kayitli uye yoksa
            self.listbox.insert(tk.END, "Kayıtlı üye yok.")
            return # Fonksiyon sonlanır

        for uye in self.kutuphane.uyeler:
            satir = f"Üye ID: {uye.uye_id} | Adı: {uye.ad}"
            self.listbox.insert(tk.END, satir) # Uye bilgisi listeye eklenir.

    # KUTUPHANEYI SIFIRLA
    def kutuphane_sifirla_islem(self):
        onay = messagebox.askyesno("Sistem Sıfırlama", "Tüm veriler silinecek. Emin misiniz?") # Kullaniciya Evet/Hayir butonlu onay penceresi acar.
        if onay:
            self.kutuphane.kutuphane_sifirla() # Arka plandaki listeleri ve JSON dosyasini temizler.
            self.kitaplari_yenile()  # Listbox'i gunceller.
            messagebox.showinfo("ÇIKTI", "Kütüphane sıfırlandı.")

    # TEMİZLİK VE ÇIKIŞ
    def kutulari_temizle(self): # İslem bittikten sonra ekrandaki giris kutularinin icini tamamen bosaltir.
        self.entry_id.delete(0, tk.END)
        self.entry_ad.delete(0, tk.END)
        self.entry_yazar.delete(0, tk.END)

    def guvenli_cikis(self):
        self.kutuphane.kaydet() # Kapatmadan once verileri JSON dosyasina kalici olarak kaydeder.
        self.pencere.quit() # Arayuz penceresini kapatir.

    def run(self):
        self.pencere.mainloop()