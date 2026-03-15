# 🎮 Video Game Sales — Analisis Data Portofolio

> **Dataset:** `vgsales.csv` — Lebih dari 16.500 judul game dari berbagai platform, publisher, genre, dan wilayah penjualan global.

---

## 📖 Latar Belakang

Industri video game adalah salah satu industri hiburan terbesar dan paling dinamis di dunia, dengan perputaran pendapatan yang melampaui industri film dan musik secara bersamaan. Setiap dekade, ekosistem platform, preferensi konsumen, dan lanskap bisnis publisher selalu mengalami pergeseran signifikan yang menarik untuk dikaji secara ilmiah menggunakan data.

Proyek ini memanfaatkan dataset historis penjualan video game global (`vgsales.csv`) yang mencakup lebih dari **16.500 judul game** dari tahun **1980 hingga 2016**, untuk menjawab pertanyaan-pertanyaan bisnis dan demografis yang relevan bagi industri gaming masa kini.

Analisis ini disusun sebagai portofolio untuk mendemonstrasikan kemampuan **pengolahan data eksploratif (EDA)**, interpretasi data multidimensi, serta penyampaian _insight_ berbasis bukti (_evidence-based insights_) yang actionable.

---

## 🎯 Objektif Analisis

| #   | Pertanyaan Analisis                                                                                           | Jenis                    |
| --- | ------------------------------------------------------------------------------------------------------------- | ------------------------ |
| 1   | Platform/konsol apa yang memiliki umur pasar paling panjang dan penjualan global tertinggi sepanjang sejarah? | Deskriptif               |
| 2   | Siapakah 5 Publisher tersukses, dan genre apa yang mendominasi pendapatan mereka?                             | Deskriptif & Preskriptif |
| 3   | Apakah terdapat perbedaan signifikan preferensi genre antara pasar Amerika Utara dan Jepang?                  | Deskriptif & Diagnostik  |
| 4   | Bagaimana tren penjualan video game global dari tahun ke tahun?                                               | Deskriptif               |
| 5   | Genre apa yang paling efisien secara komersial (volume produksi vs nilai penjualan)?                          | Deskriptif               |

---

## 🛠️ Langkah-langkah Analisis

```
1. Pemuatan & Pemeriksaan Data       → Memuat dataset, cek tipe data & missing values
2. Pra-pemrosesan Data               → Hapus baris dengan Year/Publisher kosong, konversi tipe data
3. Analisis Platform                 → Agregasi umur pasar & total penjualan per platform
4. Analisis Publisher                → Ranking top 5 publisher, breakdown genre, kalkulasi % dominasi
5. Analisis Regional                 → Agregasi penjualan per genre per region, normalisasi, heatmap
6. Analisis Bonus (Tren & Genre)     → Tren tahunan, profil volume vs nilai vs efisiensi genre
7. Visualisasi & Interpretasi        → 9 grafik interaktif + narasi insight tiap analisis
```

---

## 📊 Analisis 1 — Tren Kesuksesan Platform/Konsol

**Pertanyaan:** _"Platform/konsol apa yang memiliki umur pasar paling panjang dan menyumbang total penjualan global tertinggi?"_

**Metodologi:**

- Umur pasar dihitung dari selisih tahun rilis game **terakhir** dan **pertama** per platform (+1)
- Total penjualan global diagregasi menggunakan `groupby` + `sum`
- Bubble chart untuk memetakan korelasi antara umur pasar, jumlah game, dan total penjualan

### Visualisasi

![Top 10 Platform: Penjualan Global vs Umur Pasar](visualization/Top%2010%20Platform%20Sepanjang%20Sejarah%20dan%20Total%20Penjualan%20Global%20vs%20Umur%20Pasar.png)

![Korelasi Umur Pasar vs Penjualan (Bubble Chart)](visualization/Korelasi%20Umur%20Pasar%20vs%20Total%20Penjualan%20Global%20per%20Platform.png)

### 💡 Kesimpulan

- **PS2** adalah konsol tersukses sepanjang sejarah dengan **>1.200 juta kopi game terjual**, menunjukkan bahwa ekosistem game yang kaya dan harga konsol yang terjangkau adalah kunci dominasi pasar.
- **PC** memiliki "rentang hidup" perilisan game terpanjang (>30 tahun) karena sifatnya yang modular dan tidak bergenerasi seperti konsol.
- **Nintendo DS & Game Boy** membuktikan bahwa platform _handheld_ bisa bersaing setara dengan konsol rumah dalam hal total penjualan global.
- **Tidak ada korelasi linear** yang kuat antara umur pasar dan total penjualan — kualitas library game dan timing rilis jauh lebih menentukan.

---

## 📈 Analisis 2 — Strategi Monopoli Publisher

**Pertanyaan:** _"Siapakah 5 Publisher paling sukses, dan Genre apa yang mendominasi pendapatan mereka?"_

**Metodologi:**

- Ranking publisher berdasarkan total `Global_Sales` dengan `nlargest(5)`
- Breakdown genre per publisher menggunakan `groupby(['Publisher', 'Genre'])`
- Visualisasi horizontal bar per publisher + stacked bar % komposisi genre

### Visualisasi

![Penguasaan Genre oleh 5 Publisher Teratas](<visualization/Penguasaan%20Genre%20oleh%205%20Publisher%20Teratas%20(Penjualan%20per%20Genre).png>)

![Komposisi Genre (%) per Publisher](<visualization/Komposisi%20Genre%20(%25)%20per%20Publisher%20-%20Identifikasi%20DNA%20Bisnis%20Masing-masing.png>)

### 💡 Kesimpulan

| Publisher                | Genre Dominan                | % Kontribusi |
| ------------------------ | ---------------------------- | ------------ |
| **Nintendo**             | Platform (Super Mario, etc.) | ~23%         |
| **Electronic Arts**      | Sports (FIFA, Madden NFL)    | ~44%         |
| **Activision**           | Shooter (Call of Duty)       | ~41%         |
| **Sony Comp. Ent.**      | Racing (Gran Turismo)        | ~28%         |
| **Take-Two Interactive** | Action (GTA, Red Dead)       | ~58%         |

**Rekomendasi Preskriptif:**

> Bagi developer/studio baru, sangat tidak disarankan bersaing di genre yang sudah dimonopoli raksasa di atas (**Red Ocean**). Peluang terbesar ada di genre yang masih terfragmentasi seperti _Adventure, Strategy, Simulation_, atau dengan membangun _Hybrid Genre_ inovatif yang menarget lebih dari satu segmen sekaligus (**Blue Ocean**).

---

## 🌍 Analisis 3 — Preferensi Genre Berdasarkan Regional

**Pertanyaan:** _"Apakah terdapat perbedaan signifikan dalam preferensi genre antara pasar Amerika Utara dan Jepang?"_

**Metodologi:**

- Agregasi `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales` per genre
- Normalisasi ke persentase untuk perbandingan yang adil (_apples-to-apples_)
- Visualisasi: Grouped bar, Spotlight bar NA vs JP, Heatmap pangsa pasar

### Visualisasi

![Perbandingan Preferensi Genre Berdasarkan Region](visualization/Perbandingan%20Preferensi%20Genre%20Berdasarkan%20Region%20Pasar.png)

![Spotlight: Amerika Utara vs Jepang](visualization/Perbandingan%20Peringkat%20Genre.png)

![Heatmap Pangsa Pasar Genre per Region](<visualization/Heatmap%20Pangsa%20Pasar%20Genre%20per%20Region%20(%25).png>)

### 💡 Kesimpulan

- **Anomali Jepang terbukti nyata dan signifikan:** Satu-satunya pasar besar di mana **Role-Playing (RPG)** merajai, sementara genre **Shooter** nyaris tidak laku sama sekali.
- **Amerika Utara & Eropa identik seleranya:** Keduanya sepakat menempatkan **Action → Sports → Shooter** sebagai 3 genre teratas.
- **Implikasi Lokalisasi:**
  - Menembus Jepang → Wajib genre RPG/Platform dengan narasi kuat & desain anime-style
  - Menembus Barat → Fokus pada Action kompetitif, Sports berlisensi, atau Shooter sinematik
  - Strategi aman global → **Action-RPG** yang mampu menembus semua region

---

## ⭐ Analisis 4 — Tren Penjualan Global dari Tahun ke Tahun

### Visualisasi

![Tren Penjualan Video Game Global (1980–2016)](<visualization/Tren%20Penjualan%20Video%20Game%20Global%20dari%20Tahun%20ke%20Tahun%20(1980%E2%80%932016).png>)

### 💡 Kesimpulan

- **Era Keemasan Industri (2006–2010):** Total penjualan mencapai puncaknya, didorong oleh Nintendo Wii yang membuka pasar _casual gaming_ massal dan boom franchise FPS barat.
- **Penurunan pasca-2010 bukan keruntuhan:** Ini adalah **migrasi distribusi** dari fisik ke _digital download_ dan _mobile_, yang tidak tertangkap dalam dataset penjualan fisik ini.

---

## ⭐ Analisis 5 — Profil Genre: Volume vs Nilai vs Efisiensi

### Visualisasi

![Volume Produksi vs Nilai Penjualan vs Efisiensi per Genre](visualization/Volume%20Produksi%20vs%20Nilai%20Penjualan%20vs%20Efisiensi%20per%20Game.png)

### 💡 Kesimpulan

- **Action = Juara Volume & Nilai Total:** Paling banyak diproduksi sekaligus menghasilkan total penjualan terbesar.
- **Platform & Sports = Efisiensi Tinggi:** Rata-rata penjualan per game sangat tinggi karena didominasi _blockbuster_ mega-hits (Mario, FIFA, Wii Sports).
- **Puzzle & Strategy = Oversupplied:** Banyak game diproduksi namun return per judul sangat rendah — pasar jenuh.

---

## 📁 Struktur Repositori

```
📦 GDKB/
├── 📂 Data/
│   └── vgsales.csv              # Dataset utama (16.598 baris × 11 kolom)
├── 📂 visualization/            # Semua output grafik analisis (9 file .png)
├── 📓 dataanalytic.ipynb        # Notebook utama (EDA + visualisasi + insight)
└── 📄 README.md                 # Dokumentasi proyek ini
```

---

## 🔧 Stack Teknologi yang dipakai

| Tools              | Fungsi                               |
| ------------------ | ------------------------------------ |
| `Python 3`         | Bahasa pemrograman utama             |
| `pandas`           | Manipulasi & agregasi data           |
| `matplotlib`       | Rendering grafik dasar               |
| `seaborn`          | Visualisasi statistik tingkat lanjut |
| `Jupyter Notebook` | Environment analisis interaktif      |

---

## 👤 Informasi Penulis

|              |                                  |
| ------------ | -------------------------------- |
| **Nama**     | Muhammad Faiqul Umam Dzunnuroeni |
| **NIM**      | 24060123140136                   |
| **Kelas**    | 4E — Sistem Informasi            |
| **Instansi** | UIN Syarif Hidayatullah Jakarta  |

---

_(Portofolio Data Analysis — 2026)_
