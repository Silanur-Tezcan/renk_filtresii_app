import cv2
import numpy as np
import os

# 🔍 Zoom (yakınlaştırma) fonksiyonu
def img_zoom(img):
    # Görüntünün boyutlarını al
    height, width = img.shape[:2]

    # %25 daha büyük yap
    new_width = int(width * 1.25)
    new_height = int(height * 1.25)

    # Yeni boyuta göre yeniden boyutlandır (yakınlaştır)
    zoomed_img = cv2.resize(img, (new_width, new_height))
    return zoomed_img

def out_img(img):
    height,width=img.shape[:2]
    new_width = int(width * 0.25)
    new_height = int(height * 0.25)

    outed_img=cv2.resize(img,(new_width,new_height))
    return outed_img

def sag_alt(img):
    bilgi_satir=int(img.shape[0]*0.75)
    bilgi_sutun=int(img.shape[1]*0.75)

    new_crop=img[bilgi_satir:,bilgi_sutun:,:]
    return new_crop
# 🎨 Filtre uygulama fonksiyonu
def apply_filter(image_path, filter_type):
    # Resmi oku
    img = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)

    if img is None:
        raise ValueError("⚠️ Resim yüklenemedi!")

    # Filtre türüne göre işlem yap
    if filter_type == 'gray':  # Gri ton
        filtered = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2BGR)

    elif filter_type == 'red':  # Sadece kırmızı kanalı bırak
        filtered = img.copy()
        filtered[:, :, 0] = 0  # Mavi sıfırla
        filtered[:, :, 1] = 0  # Yeşil sıfırla

    elif filter_type == 'green':  # Sadece yeşil kanalı bırak
        filtered = img.copy()
        filtered[:, :, 0] = 0
        filtered[:, :, 2] = 0

    elif filter_type == 'blue':  # Sadece mavi kanalı bırak
        filtered = img.copy()
        filtered[:, :, 1] = 0
        filtered[:, :, 2] = 0

    elif filter_type == 'sepia':  # Eski fotoğraf efekti
        kernel = np.array([[0.272, 0.534, 0.131],
                           [0.349, 0.686, 0.168],
                           [0.393, 0.769, 0.189]])
        filtered = cv2.transform(img, kernel)
        filtered = np.clip(filtered, 0, 255).astype(np.uint8)

    elif filter_type == 'zoom':  # Yakınlaştırma
        filtered = img_zoom(img)

    elif filter_type == 'out':
        filtered=out_img(img)
    elif filter_type == 'right_crop':
        filtered=sag_alt(img)
    else:
        filtered = img  # Eğer tanınmayan bir filtre varsa orijinal resmi göster

    # Kaydedilecek dosya yolu
    output_path = os.path.join("static", "uploads", "filtered.jpg")

    # İşlenmiş resmi kaydet
    cv2.imwrite(output_path, filtered)

    return output_path
