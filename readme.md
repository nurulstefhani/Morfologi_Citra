# 🧩 Operasi Morfologi pada Citra Biner
Implementasi praktikum **Pengolahan Citra Digital (Pekan 5)** — *Operasi Morfologi pada Citra Biner* menggunakan **Python dan OpenCV**.

---

## 📘 Deskripsi

Operasi morfologi adalah teknik **pengolahan citra berbasis bentuk (shape-based image processing)**.  
Operasi ini bekerja menggunakan **structuring element (SE)** — yaitu matriks kecil (misalnya 3×3 atau 5×5) yang berfungsi untuk menentukan area tetangga (neighborhood) setiap piksel yang sedang diproses.

Citra yang digunakan umumnya adalah **citra biner**, yaitu citra dengan dua nilai piksel:
- `0` → hitam (background)
- `255` → putih (foreground / objek)

---

## 🧱 Citra Biner dan Structuring Element (SE)

### 🔹 Citra Biner
Citra biner diperoleh dari proses thresholding:
```python
_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)
```

### 🔹 Structuring Element
Structuring element berperan seperti kernel yang mengatur bentuk dan ukuran area yang diproses.
Beberapa bentuk SE umum:
- `cv2.MORPH_RECT` → persegi
- `cv2.MORPH_ELLIPSE` → elips
- `cv2.MORPH_CROSS` → silang

Contoh:
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
```

---

## ⚙️ Operasi Morfologi Dasar

### 🧩 1. **Erosion (Erosi)**
- **Konsep:** Mengikis batas objek foreground.
- **Efek:** Objek mengecil, noise kecil hilang, dan objek yang berdekatan bisa terpisah.
- **Rumus:** Piksel bernilai 1 akan tetap 1 hanya jika semua piksel di bawah SE bernilai 1.
- **Kode:**
  ```python
  erosion = cv2.erode(image_binary, kernel, iterations=1)
  ```

---

### 🧩 2. **Dilation (Dilasi)**
- **Konsep:** Memperbesar objek foreground.
- **Efek:** Objek melebar, celah kecil tertutup, objek terpisah bisa menyatu.
- **Rumus:** Piksel bernilai 0 akan menjadi 1 jika minimal satu piksel di bawah SE bernilai 1.
- **Kode:**
  ```python
  dilation = cv2.dilate(image_binary, kernel, iterations=1)
  ```

---

### 🧩 3. **Opening (Buka)**
- **Konsep:** Erosion → Dilation  
  (Menghilangkan noise di luar objek tanpa mengubah bentuk utama)
- **Rumus:** `A ∘ B = (A⊖B)⊕B`
- **Kode:**
  ```python
  opening = cv2.morphologyEx(image_binary, cv2.MORPH_OPEN, kernel)
  ```

---

### 🧩 4. **Closing (Tutup)**
- **Konsep:** Dilation → Erosion  
  (Menutup lubang kecil di dalam objek)
- **Rumus:** `A • B = (A⊕B)⊖B`
- **Kode:**
  ```python
  closing = cv2.morphologyEx(image_binary, cv2.MORPH_CLOSE, kernel)
  ```

---

## 🔍 Operasi Morfologi Turunan

### 🧩 5. **Morphological Gradient**
- **Konsep:** Dilation - Erosion  
  Menampilkan batas luar (outline) dari objek.
- **Aplikasi:** Ekstraksi boundary, deteksi tepi alternatif Sobel/Canny.
- **Kode:**
  ```python
  gradient = cv2.morphologyEx(image_binary, cv2.MORPH_GRADIENT, kernel)
  ```

---

### 🧩 6. **Top Hat dan Black Hat**
- **Top Hat:** `Original - Opening`  
  ➜ Menonjolkan objek kecil yang **lebih terang** dari background.
  ```python
  tophat = cv2.morphologyEx(image_binary, cv2.MORPH_TOPHAT, kernel)
  ```
- **Black Hat:** `Closing - Original`  
  ➜ Menonjolkan objek kecil yang **lebih gelap** dari background.
  ```python
  blackhat = cv2.morphologyEx(image_binary, cv2.MORPH_BLACKHAT, kernel)
  ```

---

## 🧠 Aplikasi Praktis

1. **Noise Removal**
   - Menggabungkan *Opening* dan *Closing* untuk membersihkan hasil thresholding.
   ```python
   cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
   cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel)
   ```

2. **Boundary Extraction**
   - Menggunakan Morphological Gradient untuk mengekstrak tepi objek.
   ```python
   boundary = cv2.morphologyEx(cleaned, cv2.MORPH_GRADIENT, kernel)
   ```

3. **Object Detection**
   - Menggunakan Top Hat atau Black Hat untuk mendeteksi area terang/gelap kecil.

---

## 📊 Ringkasan Operasi

| Operasi | Simbol | Kombinasi | Efek |
|----------|--------|------------|------|
| **Erosion** | ⊖ | - | Mengecilkan objek, hapus noise |
| **Dilation** | ⊕ | - | Memperbesar objek |
| **Opening** | ∘ | Erosion + Dilation | Hilangkan noise di background |
| **Closing** | • | Dilation + Erosion | Tutup lubang kecil di objek |
| **Gradient** | ⊕ - ⊖ | - | Ekstraksi tepi objek |
| **Top Hat** | A - (A∘B) | - | Deteksi area terang kecil |
| **Black Hat** | (A•B) - A | - | Deteksi area gelap kecil |

---

## 💻 Cara Menjalankan

1. **Pastikan Python sudah terinstal.**
2. **Install dependensi:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Jalankan program:**
   ```bash
   python morfologi_citra.py
   ```
4. Akan muncul 8 hasil operasi morfologi:
   - Original, Erosion, Dilation, Opening, Closing, Gradient, Top Hat, dan Black Hat.

---

## 📷 Contoh Input
Gunakan gambar biner sederhana seperti persegi putih di latar hitam (`gambar.jpg` sudah disertakan).

---

## 📚 Referensi Materi
**Dr. Arya Adhyaksa Waskita (2025)**  
_Pengolahan Citra Digital – Operasi Morfologi pada Citra Biner (Pekan 5)_

---

## 🧑‍💻 Disusun oleh
**Nurul Stefhani**  
UTS Pengolahan Citra Digital  
Universitas Pamulang
