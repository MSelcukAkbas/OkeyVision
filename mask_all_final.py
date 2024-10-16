import cv2
import numpy as np
import json
from concurrent.futures import ProcessPoolExecutor
from sklearn.cluster import KMeans

class ColorFilter:
    def __init__(self, image_path):
        """
        Sınıfın yapıcı metodu. Resim yolunu alır ve resmi HSV formatına çevirir.
        HSV renk kodlarını 'hsv_color_codes.json' dosyasından yükler.
        """
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        with open('data/hsv_color_codes.json', 'r') as file:
            self.data = json.load(file)

    def hsv_normalizer(self, color_list):
        """
        HSV renk listesini gruplar halinde alarak her grubun ortalamasını hesaplar.
        Gruplar 4'lü paketler şeklindedir ve ortalama HSV değeri döndürülür.
        """
        normal_list = []
        for i in range(0, len(color_list), 4):
            group = color_list[i:i + 4]
            if len(group) == 4:
                h_avg = sum(item[0] for item in group) // 4
                s_avg = sum(item[1] for item in group) // 4
                v_avg = sum(item[2] for item in group) // 4
                normal_list.append((h_avg, s_avg, v_avg))
        return normal_list
    
    def _get_color_ranges(self, colors):
        """
        Verilen HSV renk değerlerinden alt ve üst renk sınırlarını oluşturur.
        """
        lower_colors = []
        upper_colors = []

        for color in colors:
            h, s, v = color
            h = int(h * 180 / 360)  
            s = int(s * 2.55)    
            v = int(v * 2.55)       
            lower_colors.append(np.array([h - 10, max(0, s - 30), max(0, v - 30)])) 
            upper_colors.append(np.array([h + 10, 255, 255]))

        return lower_colors, upper_colors
    
    def filter_color(self, colors):
        """
        Verilen renk değerlerine göre resmi filtreleyip belirlenen renkleri içerir.
        """
        lower_colors, upper_colors = self._get_color_ranges(colors)

        masks = [cv2.inRange(self.hsv_image, lower, upper) for lower, upper in zip(lower_colors, upper_colors)]
        combined_mask = sum(masks)
        result = cv2.bitwise_and(self.image, self.image, mask=combined_mask)

        return result

    def merge_images(self, images, alpha=0.5):
        """
        Birden fazla resmi birleştirir. 'alpha' değeri resimlerin şeffaflığını belirler.
        """
        merged_image = np.zeros_like(images[0])
        for img in images:
            merged_image = cv2.addWeighted(merged_image, 1 - alpha, img, alpha, 0)

        return merged_image
    
    def process_black_(self):
        """
        Siyah bölgeleri sarıya çevirir ve sarı bölgelerdeki sayıları tespit eder.
        """
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 255, 50])
        black_mask = cv2.inRange(self.hsv_image, lower_black, upper_black)

        yellow = np.full_like(self.image, (0, 255, 255))
        black_to_yellow = cv2.bitwise_and(yellow, yellow, mask=black_mask)

        black_background = np.zeros_like(self.image)
        black_yellow_image = cv2.bitwise_or(black_to_yellow, black_background)

        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        yellow_mask = cv2.inRange(self.hsv_image, lower_yellow, upper_yellow)

        only_yellow_numbers = cv2.bitwise_and(self.image, self.image, mask=yellow_mask)

        final_image = cv2.bitwise_or(black_yellow_image, only_yellow_numbers)

        return final_image

    def get_dominant_colors(self, image, num_colors=5):
        """
        Görüntüden baskın renkleri elde eder.
        """
        resized_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2), interpolation=cv2.INTER_AREA)
        reshaped_image = resized_image.reshape((-1, 3))

        kmeans = KMeans(n_clusters=num_colors)
        kmeans.fit(reshaped_image)

        colors = kmeans.cluster_centers_.astype(int)
        return colors

    def filter_and_extract_colors(self, output_json, a=1, b=1.30, c=1.60, num_colors=5):
        """
        Görüntüyü filtreler ve renkleri çıkartır. Çıkan renk bilgilerini JSON dosyasına kaydeder.
        """
        original_image = self.image.copy()
        gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        extracted_colors = []

        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            if w > 0:
                aspect_ratio = h / w
            else:
                continue

            if b <= aspect_ratio <= c:
                stone_roi = original_image[y:y+h, x:x+w]
                dominant_colors = self.get_dominant_colors(stone_roi, num_colors=num_colors)

                extracted_colors.append({
                    'position': (x, y, w, h),
                    'dominant_colors': dominant_colors.tolist()
                })
            else:
                cv2.drawContours(original_image, [contour], -1, (0, 0, 0), thickness=cv2.FILLED)

        with open(output_json, 'w') as f:
            json.dump(extracted_colors, f, indent=4)

        output_image_path = self.image_path.replace('.jpg', '_filtered.jpg')
        cv2.imwrite(output_image_path, original_image)

        print(f"Renk bilgileri '{output_json}' dosyasına kaydedildi.")
        print(f"İşlenmiş görüntü '{output_image_path}' olarak kaydedildi.")

    def main(self, result_path: str, output_json: str):
        """
        Ana fonksiyon, HSV kodları normalize eder, renkleri filtreler ve sonucu kaydeder.
        """
        red_data, yellow_data, blue_data = self.data["red"], self.data["yellow"], self.data["blue"]
        
        with ProcessPoolExecutor() as executor:
            normalized_blue = executor.submit(self.hsv_normalizer, blue_data)
            normalized_yellow = executor.submit(self.hsv_normalizer, yellow_data)
            normalized_red = executor.submit(self.hsv_normalizer, red_data)
            processed_black = executor.submit(self.process_black_)

            try:
                blue_normalized = normalized_blue.result()  
                yellow_normalized = normalized_yellow.result()
                red_normalized = normalized_red.result()
                black_processed = processed_black.result()
            except Exception as e:
                print(f"Error saving images: {e}")

        with ProcessPoolExecutor() as executor:
            filtered_blue = executor.submit(self.filter_color, blue_normalized)
            filtered_yellow = executor.submit(self.filter_color, yellow_normalized)
            filtered_red = executor.submit(self.filter_color, red_normalized)

            try:
                blue_filtered = filtered_blue.result()  
                yellow_filtered = filtered_yellow.result()
                red_filtered = filtered_red.result()
            except Exception as e:
                print(f"Error saving images: {e}")

        try:
            cv2.imwrite(result_path.replace('.jpg', '_black_filtered.jpg'), black_processed)    
            cv2.imwrite(result_path.replace('.jpg', '_blue_filtered.jpg'), blue_filtered)    
            cv2.imwrite(result_path.replace('.jpg', '_yellow_filtered.jpg'), yellow_filtered)    
            cv2.imwrite(result_path.replace('.jpg', '_red_filtered.jpg'), red_filtered)    
        except Exception as e:
            print(f"Error saving images: {e}")

        self.filter_and_extract_colors(output_json)

if __name__ == "__main__":
    color_filter = ColorFilter(r'data\5.jpg')
    color_filter.main(r'data\5_ssss.jpg', 'renk_bilgileri.json')
