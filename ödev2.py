#adı:anas babı
#no:02190201101
import numpy as np

# Web kamerayı başlat
cap = cv2.VideoCapture(0)

while True:
    # Giriş görüntüsünü oku
    ret, frame = cap.read()

    # RGB formatından HSV formatına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Belirlenen renk aralığı (örneğin, yeşil ve mavi renk aralığı)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([80, 255, 255])

    lower_blue = np.array([90, 40, 40])
    upper_blue = np.array([150, 255, 255])

    # HSV görüntüsü üzerinde maske oluştur
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # Giriş görüntüsü ve maskeleri birleştir
    result = cv2.bitwise_and(frame, frame, mask=cv2.bitwise_not(mask_green + mask_blue))

    # Görüntüleri göster
    cv2.imshow('Original', frame)
    cv2.imshow('Result', result)

    # Çıkış için 'q' tuşuna basılmasını bekleyin
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pencereyi kapat
cap.release()
cv2.destroyAllWindows()