#no:02190201101

import cv2
import numpy as np

image = np.zeros((300, 300), dtype=np.uint8)

num_rice_grains = np.random.randint(5, 11)

for _ in range(num_rice_grains):
    x, y = np.random.randint(50, 250), np.random.randint(50, 250)
    cv2.circle(image, (x, y), 5, 255, -1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((5, 5), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

_, labels, stats, centroids = cv2.connectedComponentsWithStats(morph, connectivity=8)


total_objects = len(stats) - 1
print("Toplam pirinç sayısı:", total_objects)

result_image = cv2.cvtColor(morph, cv2.COLOR_GRAY2BGR)

for i in range(1, total_objects + 1):
    cv2.putText(result_image, str(i), (int(centroids[i][0]), int(centroids[i][1])),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow('Result', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()