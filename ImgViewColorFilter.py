import cv2
from mask_all_final import ColorFilter
import matplotlib.pyplot as plt

def show_images_with_text(images: list, titles : list):
    """
    işlenmiş görüntüleri ve başlıkları kullanarak her görüntünün üzerine metin ekler 
    ve görüntüleri gösterir.

    :param images: İşlenmiş görüntüler listesi
    :param titles: Her görüntü için başlıklar listesi
    """
    for i, title in enumerate(titles):
        ax = plt.subplot(1, 4, i + 1)
        
        img_rgb = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        position = (10, 30) 
        font_scale = 1  
        font_color = (255, 255, 255)
        font_thickness = 2 

        cv2.putText(img_rgb, title, position, font, font_scale, font_color, font_thickness, cv2.LINE_AA)
        
        ax.imshow(img_rgb)
        ax.axis('off')

    plt.tight_layout() 
    plt.show()  

if __name__ == "__main__":
    color_filter = ColorFilter(r'data\5.jpg')
    
    results = color_filter.main(r'data\5_ssss.jpg', 'renk_bilgileri.json', save=False)

    if results:
        black_processed = results["black"]
        blue_filtered = results["blue"]
        yellow_filtered = results["yellow"]
        red_filtered = results["red"]

        show_images_with_text(
            [red_filtered, blue_filtered, black_processed, yellow_filtered],
            ["Red", "Blue", "Black", "Yellow"]
        )
    else:
        print("Resimler işlenirken bir hata oluştu.")
