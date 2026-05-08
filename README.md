# Pengolahan-Citra-Digital
Studi Peningkatan Kualitas Visual Citra Digital Menggunakan *Color Enhancement* dan *Edge Detection*

👤 **Tentang Project**
Project ini disusun untuk memenuhi tugas mata kuliah Pengolahan Citra Digital. Studi kasus yang diangkat adalah optimalisasi visual pada tangkapan layar game "Soul Sealer: Calamity Rifts". Fokus utama project ini adalah meningkatkan daya tarik visual aset game melalui manipulasi domain spasial.

🎯 **Tujuan**
- Mengimplementasikan teknik peningkatan warna (vibransi) pada ruang warna HSV.
- Menerapkan *Adaptive Edge Detection* untuk mengekstraksi struktur objek 3D.
- Menciptakan efek visual artistik (*Artistic Sketch*) melalui teknik *Image Blending*.

🧠 **Landasan Teori**
1. **Citra Digital**
Representasi visual dalam bentuk data numerik yang diolah menggunakan komputer untuk mengubah atau meningkatkan kualitas informasi visualnya.

2. **HSV Color Enhancement**
Meningkatkan intensitas warna melalui manipulasi *channel* Saturation dan Value pada ruang warna HSV. Teknik ini lebih unggul dibandingkan RGB karena tidak mengubah inti warna (Hue) asli dari aset game.

3. **Edge Detection & Blending**
Menggunakan algoritma Canny untuk mendeteksi tepi objek berdasarkan perubahan kontras piksel yang tajam. Hasil deteksi kemudian dipadukan kembali dengan citra asli menggunakan metode *weighted addition* untuk menciptakan efek sketsa yang estetik.

⚙️ **Implementasi**
- **Tools:** Python, OpenCV, NumPy, Matplotlib.
- **Langkah-langkah:**
  1. Load citra digital dari direktori lokal.
  2. Konversi warna ke domain HSV dan peningkatan bobot warna.
  3. Proses deteksi tepi menggunakan parameter adaptif (Auto-Canny).
  4. Penggabungan (*Blending*) citra tepi dengan citra asli.

🖼️ **Hasil**
![Hasil Olahan Citra](Screenshot%202026-05-08%20193244.png)

📊 **Analisis**
Penerapan *Color Enhancement* berhasil memperkuat *artstyle* game yang cerah dan *stylized*. Sementara itu, *Edge Detection* yang dipadukan dengan teknik *blending* memberikan detail garis yang tegas pada objek bangunan dan karakter, menciptakan kesan visual yang lebih dalam dan artistik.

🚀 **Kesimpulan**
Manipulasi citra digital terbukti mampu memberikan nilai tambah estetika pada pengembangan visual game. Pemilihan metode yang tepat memungkinkan pengembang untuk mengoptimalkan aset grafis dengan efisien tanpa kehilangan detail asli.

💬 **Refleksi Pribadi**
Project ini memberikan pemahaman bahwa di balik setiap piksel layar terdapat logika komputasi yang sangat kuat. Mempelajari pengolahan citra membuka peluang besar dalam pengembangan teknologi grafika di masa depan.
“Bertarunglah sehancur-hancurnya selagi muda, sampai tak tersisa sedikitpun kerusakan di masa depanmu.”

📎 **Penutup**
Terima kasih telah meninjau project ini. Semoga eksplorasi ini menjadi langkah awal yang bermanfaat dalam pengembangan kemampuan di bidang teknologi.
