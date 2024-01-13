
from google.colab import files
from PIL import Image
import cv2
import numpy as np
import io
import matplotlib.pyplot as plt

def calculate_psnr(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return float('inf')
    max_pixel = 255.0
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    return psnr

# Meminta pengguna untuk mengunggah file
uploaded = files.upload()

# Baca gambar dari objek byte
gambar_byte = list(uploaded.values())[0]
original_image = Image.open(io.BytesIO(gambar_byte))

# Menampilkan gambar asli
plt.imshow(original_image)
plt.title("Original Image")
plt.show()

# Simpan gambar asli sebagai array NumPy
original_array = np.array(original_image)

# Contoh proses steganografi (silakan sesuaikan sesuai kebutuhan Anda)
compressed_array = cv2.cvtColor(original_array, cv2.COLOR_RGB2BGR)
compressed_image = Image.fromarray(compressed_array)

# Menampilkan gambar hasil steganografi
plt.imshow(compressed_image)
plt.title("Compressed Image")
plt.show()

# Menghitung PSNR
psnr_value = calculate_psnr(original_array, compressed_array)
print(f"PSNR: {psnr_value} dB")