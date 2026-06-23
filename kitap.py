class Kitap:
    def __init__(self, kitap_id, ad, yazar, oduncte=False, uye_id=None):
        self.kitap_id = kitap_id
        self.ad = ad
        self.yazar = yazar
        self.oduncte = oduncte # Kitabın oduncte degil rafta oldugunu gösterir.
        self.uye_id = uye_id  # Kitap raftayken None (boş), oduncteyse alan uyenin ID'si olacak