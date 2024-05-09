import numpy as np
import cv2

arr = (np.arange(0, 400*600*3).reshape([400, 600, 3]) % 0xFF).astype(dtype=np.uint8)
cv2.imshow("Okienko", arr)
cv2.waitKey(0)
cv2.destroyAllWindows()