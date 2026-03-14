# Analisis Data Penjualan Video Game Global (Portfolio)

Proyek analisis data **Video Game Sales**! Proyek ini mendemonstrasikan pengolahan data eksploratif (EDA) menggunakan library Python (Pandas, Matplotlib, Seaborn) untuk menggali _insight_ penting seputar sejarah tren platform game dan monopoli para pubisher tersukses di dunia.

---

## 🎯 Objektif Analisis

Analisis ini difokuskan pada dua topik utama bisnis di industri _gaming_:

1. **Tren Kesuksesan Platform/Konsol**: Platform apa yang paling bersejarah, memiliki siklus hidup (umur pasar) paling panjang, dan menyumbang angka penjualan terbesar sepanjang masa?
2. **Strategi Monopoli Market Publisher**: Siapa 5 _Publisher_ paling elit di dunia, dan bagaimana strategi penguasaan (_Golden Genre_) mereka pada genre-genre game spesifik?

---

## 📊 1. Tren Kesuksesan Platform (Fokus Sejarah)

Berdasarkan dataset `vgsales.csv`, saya mengukur gabungan **Total Penjualan Global** (Juta Kopi) berbanding lurus dengan **Umur Pasar** masing-masing konsol (dihitung dari rilis perdana hingga game terakhirnya di dataset).

### Hasil Visualisasi:

![Top 10 Platform Sepanjang Sejarah](/imgplot/plot1.png)

### 💡 Key Insights:

- **Sang Raja Konsol (PS2)**: PlayStation 2 (PS2) memuncaki tahta penjualan konsol sepanjang sejarah (mencetak > 1.2 Miliar kopi game terjual) dengan ekosistem produktif yang panjang selama kira-kira 12 tahun.
- **Persistensi PC**: Jika dilihat secara garis umur, ekosistem **PC (Personal Computer)** adalah satu-satunya platform yang rentang hidupnya terentang lurus dan adaptif melewati > 30 tahun (berbeda dengan konsol yang bersifat generasional dan terganti setiap 7-10 tahun).
- **Perang Sengit Generasi ke-7**: X360, PS3, dan Wii mencatatkan kesuksesan luar biasa dengan rentang hidup umur konsol mereka yang seragam di angka rata-rata 10 hingga 11 tahun.

---

## 📈 2. Strategi Monopoli _Publisher_ (Fokus Bisnis)

Pada tahapan ini saya menyortir **Top 5 Publisher Global** dan membelah pendapatan mereka untuk melihat _Genre_ mana yang menyumbang pundi-pundi uang terbesar bagi kelima raksasa ini _(Action, Sports, Shooter, dll)._

### Hasil Visualisasi:

![Penguasaan Genre oleh 5 Publisher Teratas](/imgplot/plot2.png)

### 💡 Key Insights & Rekomendasi Bisnis:

Analisis membuktikan bahwa raksasa _gaming_ sengaja bersikap spesialis dan memonopoli "lahan emas" (_Golden Genre_) tertentu untuk meminimalisir kompetitor.

- **Nintendo**: Dominator mutlak untuk genre **Platform** (IP _Super Mario_) dan mahir membagi kekuatannya di ranah keluarga/RPG (_Pokemon/Zelda_).
- **Electronic Arts (EA)**: Nyaris setengah (+/- 43%) portofolio keuangan mereka bersumber tunggal dan absolut dari monopoli game olahraga (**Sports**), dipotori oleh magnet utama seperti _FIFA_ dan _Madden NFL_.
- **Activision**: Bertumpu kokoh sebesar 41% dari kejayaan game tembak-menembak bergenre **Shooter**, nyaris mustahil ditandingi berkat waralaba raksasa _Call of Duty_.
- **Take-Two Interactive**: Penguasa teritori genre **Action** (+/- 57% total profit). Monopoli penuh ditopang _Grand Theft Auto (GTA)_.
- **Sony**: Lebih fleksibel, namun sangat menonjol merengkuh pasar **Racing** (_Gran Turismo_) dipadu genre Action.

**Rekomendasi Preskriptif (_Actionable Advice_):**

> Bagi developer/studio pemula atau _publisher_ bersenjata (_budget_) menengah, disarankan untuk mencari **Blue Ocean** (Area kosong minim saingan). Sangat bunuh diri (_Red Ocean_) jika nekat membuat game bola mainstream untuk meruntuhkan EA (Sports), atau melawan tembak-tembakan raksasa Activision. Mulailah mengorbit di Genre bebas yang tidak mereka sentuh terlalu dalam seperti genre _Adventure_, _Strategy_, atau ciptakan kombinasi _Sub-genre hybrid_ yang unik.

---

### 🔧 Alat & Teknologi yang digunakan

- **Bahasa Pemrograman**: Python 3
- **Workspace**: Jupyter Notebook (`analytic.ipynb`)
- **Libraries Utama**: Pandas (Data Wrangling), Matplotlib & Seaborn (Visualisasi)

_(Portofolio Data Analysis - 2026)_
