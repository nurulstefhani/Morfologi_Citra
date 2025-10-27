# 🧩 Operasi Morfologi pada Citra Biner

Proyek ini merupakan implementasi praktikum dari materi **Pengolahan Citra Digital - Operasi Morfologi** menggunakan **Python dan OpenCV**.

## 📘 Deskripsi
Operasi morfologi adalah teknik pengolahan citra berbasis bentuk menggunakan *structuring element (SE)*.  
Beberapa operasi utama:
- **Erosion**: Mengikis tepi objek.
- **Dilation**: Memperbesar area objek.
- **Opening**: Erosion diikuti Dilation (menghilangkan noise kecil).
- **Closing**: Dilation diikuti Erosion (menutup lubang kecil).
- **Gradient, Top Hat, Black Hat** untuk mendeteksi tepi atau detail halus.

## 💻 Cara Menjalankan
1. Pastikan Python sudah terinstal.
2. Install dependensi:
   ```bash
   pip install -r requirements.txt
