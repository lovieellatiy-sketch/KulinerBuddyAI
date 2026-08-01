# 🍲 KulinerBuddyAI — Smart Culinary & Dining Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Prototype-orange.svg)]()
![GitHub stars](https://img.shields.io/github/stars/lovieellatiy-sketch/KulinerBuddyAI?style=social)
![GitHub forks](https://img.shields.io/github/forks/lovieellatiy-sketch/KulinerBuddyAI?style=social)
![GitHub issues](https://img.shields.io/github/issues/lovieellatiy-sketch/KulinerBuddyAI)
![GitHub last commit](https://img.shields.io/github/last-commit/lovieellatiy-sketch/KulinerBuddyAI)

---

# 🍽️ KulinerBuddyAI

**KulinerBuddyAI** adalah asisten kuliner berbasis **Artificial Intelligence (AI)** yang membantu pengguna menemukan menu makanan, kuliner khas daerah, serta rekomendasi tempat makan terbaik berdasarkan **lokasi, anggaran, dan preferensi pribadi** melalui percakapan yang alami (*Natural Language Processing*).

---

# 📑 Daftar Isi

- [Latar Belakang](#-latar-belakang)
- [Target Pengguna](#-target-pengguna)
- [Fitur Utama](#-fitur-utama)
- [Teknologi](#-teknologi)
- [Struktur Project](#-struktur-project)
- [Tampilan Antarmuka](#-tampilan-antarmuka-ui)
- [Contoh Penggunaan](#-contoh-penggunaan)
- [Cara Instalasi](#-cara-instalasi)
- [Roadmap](#-roadmap)
- [Kontribusi](#-kontribusi)
- [Lisensi](#-lisensi)
- [Author](#-author)

---

# 💡 Latar Belakang

Sering kali masyarakat maupun wisatawan menghabiskan banyak waktu hanya untuk menentukan pilihan makanan. Selain itu, tidak sedikit pengguna yang kesulitan menemukan tempat makan yang sesuai dengan kebutuhan seperti **Halal**, **Vegetarian**, **budget tertentu**, atau lokasi yang dekat.

**KulinerBuddyAI** hadir sebagai solusi berbasis AI yang mampu memberikan rekomendasi makanan secara cepat, personal, dan interaktif sehingga proses memilih makanan menjadi lebih mudah dan menyenangkan.

---

# 🎯 Target Pengguna

### 🧳 Wisatawan

- Menemukan makanan khas daerah
- Mencari hidden gem
- Mendapat rekomendasi restoran terbaik

### 🍜 Foodies

- Menjelajahi kuliner baru
- Berdasarkan rating tertinggi
- Berdasarkan suasana tempat

### 👨‍💼 Pekerja & Mahasiswa

- Menentukan menu makan harian
- Budget-friendly
- Tempat makan terdekat

### 🥗 Pengguna Diet Khusus

- Halal
- Vegetarian
- Vegan
- Bebas Alergen

---

# ✨ Fitur Utama

## 📍 Rekomendasi Berdasarkan Lokasi

Menampilkan restoran terdekat lengkap dengan:

- 📌 Jarak
- ⭐ Rating
- 💰 Estimasi harga
- 🕒 Jam operasional

---

## 💸 Filter Budget

Contoh pencarian:

> Cari makan siang di bawah Rp20.000

---

## 🥗 Filter Diet Khusus

Mendukung pencarian:

- Halal
- Vegetarian
- Vegan
- Child Friendly
- Open 24 Hours

---

## 🎲 Bingung Mau Makan Apa?

AI akan memberikan rekomendasi menu secara acak sesuai preferensi pengguna.

---

## 🗺️ Integrasi Google Maps

Menyediakan:

- Ringkasan ulasan
- Rating restoran
- Navigasi menuju lokasi

---

## 💬 Natural Language Chat

Contoh:

> Cari ayam geprek pedas dekat kampus

atau

> Saya ingin makan seafood malam ini dengan budget 50 ribu.

---

# 🛠️ Teknologi

| Teknologi | Fungsi |
|-----------|--------|
| Python 3.9+ | Bahasa Pemrograman |
| OpenAI GPT / Google Gemini | AI Chatbot |
| Streamlit | User Interface |
| Google Maps Places API | Data Lokasi |
| Pandas | Pengolahan Data |
| NLP | Natural Language Processing |

---

# 📂 Struktur Project

```text
KulinerBuddyAI/
│
├── assets/
│   └── images/
│
├── data/
├── models/
├── services/
├── utils/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🎨 Tampilan Antarmuka (UI)

<p align="center">
<img src="https://github.com/lovieellatiy-sketch/KulinerBuddyAI/blob/main/robot.png" width="800">
</p>

---

# 💬 Contoh Penggunaan

### 👤 User

```text
Cari makan siang pedas di bawah Rp20.000 dekat saya
```

### 🤖 KulinerBuddyAI

```text
🍜 Berikut rekomendasi untuk Anda

1. Ayam Geprek Pak Budi ⭐ 4.8
💰 Rp18.000
📍 700 meter

2. Seblak Juara ⭐ 4.7
💰 Rp15.000
📍 900 meter

3. Bakso Favorit ⭐ 4.6
💰 Rp20.000
📍 1.2 km

Apakah Anda ingin melihat rute Google Maps?
```

---

# 🚀 Cara Instalasi

## Prasyarat

- Python 3.9+
- Git
- OpenAI API Key atau Google Gemini API
- Google Maps API (Opsional)

---

## Clone Repository

```bash
git clone https://github.com/lovieellatiy-sketch/KulinerBuddyAI.git

cd KulinerBuddyAI
```

---

## Membuat Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## Install Dependency

```bash
pip install -r requirements.txt
```

---

## Konfigurasi Environment

Buat file **.env**

```env
OPENAI_API_KEY=your_openai_api_key

GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

---

## Menjalankan Program

Jika menggunakan Python

```bash
python main.py
```

Jika menggunakan Streamlit

```bash
streamlit run app.py
```

---

# 🛣️ Roadmap

- [x] AI Chatbot
- [x] Rekomendasi berdasarkan lokasi
- [x] Filter Budget
- [x] Filter Halal
- [x] Filter Vegetarian
- [x] Bingung Mau Makan Apa
- [ ] Login Pengguna
- [ ] Riwayat Pencarian
- [ ] Integrasi Google Maps
- [ ] Voice Assistant
- [ ] AI Personal Recommendation
- [ ] Dark Mode

---

# 🤝 Kontribusi

Kontribusi sangat terbuka.

1. Fork repository

2. Buat branch baru

```bash
git checkout -b fitur-baru
```

3. Commit perubahan

```bash
git commit -m "Menambahkan fitur baru"
```

4. Push ke GitHub

```bash
git push origin fitur-baru
```

5. Buat Pull Request

---

# 📄 Lisensi

Project ini menggunakan **MIT License**.

Silakan menggunakan, memodifikasi, dan mendistribusikan project ini sesuai ketentuan lisensi MIT.

---

# 👩‍💻 Author

**Lovieella**

📧 Email : lovieella.tiy@gmail.com

🐙 GitHub : https://github.com/lovieellatiy-sketch

---

## ⭐ Dukungan

Apabila project ini bermanfaat, jangan lupa berikan **Star ⭐** pada repository ini.

Terima kasih telah menggunakan **KulinerBuddyAI**.

**Happy Coding! 🚀🍜**
