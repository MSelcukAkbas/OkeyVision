# Color Group Visualization

Bu proje, okey ıstakasındaki taşları renklerine göre ayırarak, her bir taşın koordinat bilgileri ile birlikte kaydedilmesini sağlamaktadır. Taşların renkleri, benzerliklerine göre gruplandırılarak görsel bir biçimde sunulmaktadır.

## Özellikler

- JSON dosyasından taşların renk bilgilerini yükleme
- Taşlar arası benzerlik hesaplama
- Benzer renkleri gruplama ve görselleştirme
- Matplotlib kullanarak renk gruplarını çizme

## Gereksinimler

- Python 3.x
- Matplotlib
- NumPy
- Opencv

## Kurulum

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install matplotlib numpy opencv-python
```

# Proje Kullanım Kılavuzu

Bu kılavuz, projenizin nasıl kullanılacağını adım adım açıklamaktadır.

## 1. Gerekli Dosyaları Hazırlama

### `hsv_color_codes.json` Dosyasını Ekleme
Proje dizinine `hsv_color_codes.json` dosyasını ekleyin. Bu dosya, kullanmak istediğiniz HSV renk kodlarını içermelidir. Dosya yapısı aşağıdaki gibi olmalıdır:

```json
{
    "red": [
        [354, 75, 61],
        [353, 87, 62]
    ],
    "yellow": [
        [30, 100, 100],
        [31, 255, 255]
    ],
    "blue": [
        [90, 100, 100],
        [120, 255, 255]
    ]
}
```

Bu yapıda, her renk için bir dizi HSV değeri tanımlanmalıdır.

## 2. Programı Çalıştırma

### `mask_all_final.py` Dosyasını Çalıştırma
1. Terminal veya komut istemcisini açın.
2. Proje dizinine gidin. Örneğin:
   ```bash
   cd /path/to/your/project
   ```
3. Aşağıdaki komutu kullanarak `mask_all_final.py` dosyasını çalıştırın:
   ```bash
   python mask_all_final.py
   ```

## 3. Çıktıları Kontrol Etme

Program başarıyla çalıştıktan sonra belirtilen dizine aşağıdaki dosyalar kaydedilecektir:

- **5 Farklı .jpg Dosyası:** Her biri farklı renk filtreleri uygulanmış görüntülerdir.
  - Örnek dosya isimleri:
    - `5_black_filtered.jpg`
    - `5_blue_filtered.jpg`
    - `5_yellow_filtered.jpg`
    - `5_red_filtered.jpg`
    - `5_filtered.jpg`
  
- **1 Adet JSON Dosyası:** İşlenmiş renk bilgilerini içeren dosya.
  - Örnek dosya adı: `renk_bilgileri.json`

### Çıktı Dosyalarının İçeriği
- **.jpg Dosyaları:** Her bir dosya, görüntüdeki belirli renklerin filtrelenmiş hallerini içerir.
- **JSON Dosyası:** Görüntüde tespit edilen nesnelerin konum bilgileri ve baskın renkleri hakkında detaylar içerir. Örnek bir JSON yapısı aşağıdaki gibidir:
  
```json
[
    {
        "position": [x, y, width, height],
        "dominant_colors": [[r1, g1, b1], [r2, g2, b2], ...]
    },
    ...
]
```

## 4. Hata Ayıklama

Eğer program çalışırken bir hata ile karşılaşırsanız, aşağıdaki kontrol listesine göz atabilirsiniz:

- `hsv_color_codes.json` dosyasının doğru dizinde ve doğru formatta olduğundan emin olun.
- Görüntü dosyasının yolu ve adı doğru olarak ayarlandığından emin olun.
- Python ve gerekli kütüphanelerin (OpenCV, NumPy, JSON, vb.) kurulu olduğundan emin olun.

## Sonucu Görselleştirme
- **`show_images_with_text(images, titles)`**: 
  - Bu fonksiyon, işlenmiş görüntüleri ve başlıkları kullanarak her görüntünün üzerine metin ekler ve görselleştirir. 
  - `images`: Gösterilecek görüntülerin listesi.
  - `titles`: Her görüntü için başlıklar listesi. 
  - Fonksiyon, her görüntüyü bir alt grafikte gösterir ve metin bilgilerini belirli bir konumda yerleştirir.

- **Ana Kod Bloku (`if __name__ == "__main__":`)**:
  - `ColorFilter` sınıfından bir nesne oluşturur ve belirtilen görsel üzerinde renk filtreleme işlemlerini başlatır.
  - `results`: Renk filtreleme işleminden dönen sonuçları tutar.
  - Eğer sonuçlar başarılı bir şekilde dönerse, siyah, mavi, sarı ve kırmızı filtrelenmiş görüntüleri `show_images_with_text` fonksiyonu ile gösterir.
  - Aksi halde, bir hata mesajı iletilir.

## Katkıda Bulunma

Herhangi bir öneri veya katkıda bulunmak isterseniz, lütfen aşağıdan iletişime geçin.

- E-posta: [akbasselcuk32@gmail.com](mailto:akbasselcuk32@gmail.com)
- LinkedIn: [Mustafa Selçuk Akbaş](https://linkedin.com/in/mustafa-selcuk-akbas)


