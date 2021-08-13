!pip install opencv-python

import cv2
import numpy as np

img1 = np.zeros((512, 512, 3), np.uint8)

#cv2.line(img1, (0, 99), (99, 0), (225, 2, 3), 600)
cv2.line(img1, (500, 500), (12, 12), (1, 20, 300), 300)
cv2.circle(img1, (250, 250), 15, (255,255,0), 250)
cv2.putText(img1, 'ARTH2020', (172, 260), cv2.FONT_HERSHEY_SIMPLEX, 1, (128,128,0), 2)

cv2.imshow('testing', img1)
cv2.waitKey()
cv2.destroyAllWindows()
