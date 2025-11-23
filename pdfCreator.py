from fpdf import FPDF
import os

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Teknik Rapor: Otonom Araclar Icin Dinamik BEV Sistemi', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Sayfa {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 6, body)
        self.ln()

    def add_figure(self, image_path, caption):
        # Sayfanın kalan kısmını kontrol et, sığmazsa yeni sayfaya geç
        if self.get_y() > 200: 
            self.add_page()
            
        try:
            # Resmi ortalamak için x koordinatını hesapla (A4 genişliği ~210mm)
            # Resmi 150mm genişliğinde ayarlıyoruz
            img_width = 150
            x_pos = (210 - img_width) / 2
            
            # image(dosya_yolu, x, y, w)
            self.image(image_path, x=x_pos, w=img_width)
            self.ln(2) # Resimden sonra az boşluk
            
            # Resim Altı Yazısı (Caption)
            self.set_font('Arial', 'I', 10) # İtalik font
            self.cell(0, 10, caption, 0, 1, 'C') # Ortalanmış yazı
            self.ln(5)
        except Exception as e:
            print(f"UYARI: '{image_path}' bulunamadi veya yuklenemedi. ({e})")
            self.set_font('Arial', 'I', 10)
            self.cell(0, 10, f"[Gorsel Eksik: {caption}]", 0, 1, 'C')
            self.ln(5)

def tr_to_eng(text):
    replacements = {
        'ş': 's', 'Ş': 'S', 'ı': 'i', 'İ': 'I', 'ğ': 'g', 'Ğ': 'G',
        'ü': 'u', 'Ü': 'U', 'ö': 'o', 'Ö': 'O', 'ç': 'c', 'Ç': 'C'
    }
    for tr, eng in replacements.items():
        text = text.replace(tr, eng)
    return text

pdf = PDF()
pdf.add_page()

# --- İÇERİK TANIMLARI ---

title = "OTONOM ARACLAR ICIN DINAMIK SENSOR FUZYONU DESTEKLI ROBUST TERS PERSPEKTIF HARITALAMA (IPM) SISTEMI"

ozet = """OZET
Bu teknik rapor, otonom yaris araclarinda kullanilan statik kus bakisi (Bird's Eye View - BEV) goruntu olusturma yontemlerinin kisitlamalarini ele almakta ve ZED 2i stereo kamera ile IMU verilerini birlestiren dinamik, geometrik bir projeksiyon yontemi onermektedir. Onerilen sistem, arac dinamiginden (yunuslama/pitch ve yatma/roll) kaynaklanan goruntu bozulmalarini gercek zamanli olarak kompanse ederek, manuel kalibrasyon ihtiyacini ortadan kaldirmayi amaclamaktadir."""

bolum1 = """BOLUM 1: GIRIS VE PROBLEM TANIMI

1.1. Mevcut Durum Analizi
Mevcut sistemde, kamera kalibrasyonu ve BEV donusumu "Statik Homografi" yontemine dayanmaktadir. Kullanilan yaklasimda, goruntunun kaynak noktalari (src) manuel olarak secilen piksel koordinatlari ile sabitlenmistir. Donusum parametresi olarak fiziksel karsiligi olmayan ve deneme-yanilma yoluyla bulunan soyut bir 'd' degeri kullanilmaktadir.

1.2. Problem Tanimi
Mevcut manuel yontem asagidaki kritik sorunlara yol acmaktadir:
1. Dinamik Hatalar: Arac hizlandiginda veya fren yaptiginda suspansiyon sistemi aracin pitch (yunuslama) acisini degistirir. Statik yontem bu degisimi algilayamaz.
2. Kirilganlik: Kameranin montaj acisindaki en ufak bir fiziksel kayma, tum sistemin yeniden manuel ayarlanmasini gerektirir.
3. Olceksizlik: 'd' parametresi metrik bir dogruluga sahip degildir. Bu durum Pure Pursuit algoritmasinin mesafe hesaplamalarinda tutarsizlik yaratir.

1.3. Calismanin Amaci
Bu calismanin amaci, ZED 2i kamerasinin stereo derinlik ve IMU sensorlerini kullanarak, manuel mudahale gerektirmeyen, arac hareketlerine karsi dayanikli (robust) ve metrik olarak dogru bir otomatik BEV sistemi gelistirmektir."""

bolum2 = """BOLUM 2: TEORIK ALTYAPI

2.1. Pinhole Kamera Modeli ve IPM
Ters Perspektif Haritalama (IPM), 3D dunyayi 2D goruntu duzlemine iz dusuren kamera modelinin tersine cevrilmesidir. Geleneksel yontemlerde bu, yerde bilinen bir desenin homografi matrisinin hesaplanmasiyla yapilir.

2.2. Sensor Fuzyonu (Goruntu + IMU)
Kamera egiminin (pitch) hesaplanmasi icin iki yontem vardir:
1. Goruntu Tabanli: Ufuk noktasini bulmak. Isik kosullarindan etkilenir.
2. Sensor Tabanli (Onerilen): ZED 2i IMU sensorunden egimi dogrudan okumak. Bu calisma, deterministik oldugu icin bu yontemi benimsemistir."""

bolum3 = """BOLUM 3: METODOLOJI (DINAMIK GEOMETRIK PROJEKSIYON)

Onerilen sistem, "sanal bir yer duzlemi" olusturma prensibine dayanir.

3.1. Algoritma Akisi
1. Intrinsics Alimi: ZED SDK'dan odak uzakligi (fx, fy) alinir.
2. Extrinsics Guncellemesi: IMU'dan Pitch ve Roll acilari 100Hz hizinda alinir.
3. Sanal Dunya Tanimi: Aracin onundeki alanin (ROI) 3D koordinatlari tanimlanir.
4. Reprojection: 3D dunya noktalari, guncel rotasyon matrisi ve kamera matrisi kullanilarak o anki goruntudeki piksellere donusturulur.
5. Dinamik Homografi: Hesaplanan dinamik pikseller ile sabit cikti pikselleri arasinda donusum matrisi olusturulur."""

bolum4 = """BOLUM 4: KARSILASTIRMALI ANALIZ

Kriter                  | Eski Manuel Yontem       | Yeni Dinamik Yontem
------------------------|--------------------------|----------------------
Referans Kaynagi        | Statik Pikseller         | Fiziksel Dunya (3D)
Pitch (Egim) Tepkisi    | Yok (Hata olusur)        | Tam Otomatik Duzeltme
Kalibrasyon Sureci      | Manuel (Zor)             | Otomatik
Olcek (Scale)           | Bilinmiyor (Rastgele)    | Metrik (1m = 40px)
Dayaniklilik            | Kirilgan                 | Robust (Guclu)"""

bolum5 = """BOLUM 5: SONUC

Bu calisma, ZED 2i kamerasinin stereo ve atalet sensorlerini kullanarak Dinamik Geometrik Projeksiyon tabanli bir BEV sistemi gelistirmistir. Manuel 'src' noktasi secimi ve 'd' parametresi ayari tamamen ortadan kaldirilmis, arac ivmelenmeleri sirasinda olusan kamera acisi degisimleri IMU verisi ile kompanse edilmistir."""


# --- PDF'E YAZDIRMA KISMI (Burayı düzelttim) ---

# Başlık ve Özet
pdf.chapter_title(tr_to_eng(title))
pdf.chapter_body(tr_to_eng(ozet))

# Bölüm 1 ve 2
pdf.chapter_body(tr_to_eng(bolum1))
pdf.chapter_body(tr_to_eng(bolum2))

# Bölüm 3 (Metodoloji)
pdf.chapter_body(tr_to_eng(bolum3))

# GÖRSELİ BURAYA EKLİYORUZ (Metodolojiden hemen sonra mantıklı olur)
# Not: 'CODEblog.png' dosyasının bu script ile aynı klasörde olması gerekir.
pdf.add_figure('CODEblog.png', 'Sekil 1: Onerilen Dinamik Projeksiyon Algoritmasi')

# Bölüm 4 ve 5
pdf.chapter_body(tr_to_eng(bolum4))
pdf.chapter_body(tr_to_eng(bolum5))

# Dosyayı kaydet
file_name = "Otonom_BEV_Tezi_Final.pdf"
pdf.output(file_name)
print(f"PDF basariyla olusturuldu: {file_name}")