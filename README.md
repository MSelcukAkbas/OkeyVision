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

## Kurulum

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırın:

```bash
pip install matplotlib numpy
```

## Kullanım

1. `hsv_color_codes.json` dosyasını proje dizinine ekleyin. Dosya yapısı aşağıdaki gibi olmalıdır:

```json
{
    "red": [
        [
            354,
            75,
            61
        ],
        [
            353,
            87,
            62
        ],
        ....
}
```

2. `mask_all_final.py` dosyasını çalıştırın:

```bash
mask_all_final.py
```

3. Belirtilen Dizine 5 Farklı formda .jpg ve 1 adet json dosyası kayıt edilecektir. 

## Katkıda Bulunma

Herhangi bir öneri veya katkıda bulunmak isterseniz, lütfen aşağıdan iletişime geçin.

- E-posta: [akbasselcuk32@gmail.com](mailto:akbasselcuk32@gmail.com)
- LinkedIn: [Mustafa Selçuk Akbaş](https://linkedin.com/in/mustafa-selcuk-akbas)


