import cv2
import numpy as np
import matplotlib.pyplot as plt

def auto_canny(image, sigma=0.33):
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged

# Konfigurasi path gambar
img_path = r'C:\Users\LENOVO\OneDrive\Documents\PCD_Roblox_Project\assets\game_scene.png'

# Membaca citra
img_bgr = cv2.imread(img_path)

if img_bgr is not None:
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    
    # 1. Color Enhancement (HSV Space)
    hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv)
    s = np.clip(s.astype(np.int16) + 40, 0, 255).astype(np.uint8)
    v = np.clip(v.astype(np.int16) + 20, 0, 255).astype(np.uint8)
    hsv_enhanced = cv2.merge((h, s, v))
    img_enhanced = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2RGB)
    
    # 2. Adaptive Edge Detection
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_blurred = cv2.GaussianBlur(img_gray, (3, 3), 0)
    img_edges = auto_canny(img_blurred)
    
    # 3. Image Blending (Artistic Sketch Effect)
    edges_inv = cv2.bitwise_not(img_edges)
    edges_color = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2RGB)
    img_sketch = cv2.addWeighted(img_enhanced, 1.0, edges_color, 0.5, 0)
    
    # Visualisasi Output
    plt.figure(figsize=(15, 6))
    
    plt.subplot(1, 3, 1)
    plt.imshow(img_rgb)
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.imshow(img_enhanced)
    plt.title('Color Enhancement')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.imshow(img_sketch)
    plt.title('Artistic Edge Sketch')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
else:
    print("Error: Image file not found.")