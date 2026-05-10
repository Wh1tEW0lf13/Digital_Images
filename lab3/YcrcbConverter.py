import cv2
import numpy as np
import matplotlib.pyplot as plt

class YcrcbConverter:
    def convert(image_path):
        image_bgr = cv2.imread(image_path)

        image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
        bias = np.array([0, 128, 128])

        transformation_matrix = np.array([
            [0.229, 0.587, 0.114],
            [0.500, -0.418, -0.082],
            [-0.168, -0.331, 0.500]
        ])

        image_ycrcb_float = np.dot(image_rgb.astype(np.float32), transformation_matrix.T) + bias
        image_ycrcb_clipped = np.clip(image_ycrcb_float, 0, 255)
        image_ycrcb = image_ycrcb_clipped.astype(np.uint8)
        return image_ycrcb
