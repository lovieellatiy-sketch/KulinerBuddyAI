# 🍲 KulinerBuddyAI — Smart Culinary & Dining Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Prototype-orange.svg)]()
![GitHub stars](https://img.shields.io/github/stars/USERNAME/KulinerBuddyAI?style=social)
![GitHub forks](https://img.shields.io/github/forks/USERNAME/KulinerBuddyAI?style=social)
![GitHub issues](https://img.shields.io/github/issues/USERNAME/KulinerBuddyAI)
![GitHub last commit](https://img.shields.io/github/last-commit/USERNAME/KulinerBuddyAI)

**KulinerBuddyAI** adalah asisten kuliner berbasis Artificial Intelligence (AI) yang membantu pengguna menemukan menu makanan, kuliner khas daerah, serta rekomendasi tempat makan terbaik berdasarkan lokasi, anggaran, dan preferensi pribadi melalui percakapan yang alami (*Natural Language Processing*).

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

Banyak orang sering menghabiskan waktu hanya untuk menjawab pertanyaan sederhana:

> **"Hari ini makan apa?"**

Selain itu, wisatawan maupun masyarakat umum juga sering mengalami kesulitan menemukan tempat makan yang sesuai dengan kebutuhan, seperti:

- Halal
- Vegetarian/Vegan
- Budget tertentu
- Dekat dari lokasi
- Buka 24 jam
- Cocok untuk keluarga

**KulinerBuddyAI** hadir sebagai solusi berbasis AI yang mampu memberikan rekomendasi makanan secara cepat, personal, dan interaktif.

---

# 🎯 Target Pengguna

### 🧳 Wisatawan

- Mencari makanan khas daerah
- Menemukan hidden gem
- Mendapat rekomendasi restoran terbaik

### 🍔 Foodies

- Mencari tempat makan baru
- Berdasarkan rating tertinggi
- Berdasarkan suasana tempat

### 👨‍💼 Pekerja & Mahasiswa

- Menentukan menu harian
- Budget-friendly
- Dekat dari lokasi

### 🥗 Pengguna Diet Khusus

- Halal
- Vegetarian
- Vegan
- Bebas Alergen

---

# ✨ Fitur Utama

## 📍 Rekomendasi Berdasarkan Lokasi

Menampilkan restoran terdekat lengkap dengan:

- Jarak
- Rating
- Kisaran harga
- Jam operasional

---

## 💰 Filter Budget

Contoh:

> Cari makan siang di bawah Rp20.000

---

## 🥗 Filter Kebutuhan Khusus

Mendukung pencarian:

- Halal
- Vegetarian
- Vegan
- Child Friendly
- Open 24 Hours

---

## 🎲 Bingung Mau Makan Apa?

AI akan memilihkan menu secara acak sesuai preferensi pengguna.

---

## 🗺 Integrasi Google Maps

Menampilkan:

- Rating
- Review Singkat
- Navigasi Google Maps

---

## 💬 Natural Language Chat

Contoh:

> Cari ayam geprek pedas dekat kampus

atau

> Saya ingin makan seafood malam ini dengan budget 50 ribu.

---

# 🛠 Teknologi

| Teknologi | Fungsi |
|-----------|--------|
| Python 3.9+ | Bahasa Pemrograman |
| OpenAI GPT / Google Gemini | AI Chatbot |
| Streamlit | User Interface |
| Google Maps Places API | Data Lokasi |
| Pandas | Pengolahan Data |
| NLP | Pemrosesan Bahasa Alami |

---

# 📂 Struktur Project

```text
KulinerBuddyAI/
│
├── assets/
│   ├── images/
│   └── icons/
│
├── data/
│
├── models/
│
├── services/
│
├── utils/
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🎨 Tampilan Antarmuka (UI)

| Welcome Screen | Chat Recommendation | Detail Restaurant |
|:--------------:|:------------------:|:----------------:|
| ![](assets/images/home.png) | ![](assets/images/chat.png) | ![](assets/images/detail.png) |

> **Catatan:** Ganti gambar di atas dengan screenshot aplikasi Anda.

---

# 💬 Contoh Penggunaan

### User

```
Cari makan siang pedas di bawah Rp20.000 dekat saya
```

### KulinerBuddyAI

```
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
- OpenAI API Key / Gemini API
- Google Maps API (Opsional)

---

## Clone Repository

```bash
git clone https://github.com/USERNAME/KulinerBuddyAI.git

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

Linux / macOS

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

## Jalankan Program

```bash
python main.py
```

atau jika menggunakan Streamlit

```bash
streamlit run app.py
```

---

# 🛣 Roadmap

- [x] Chatbot AI
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

Langkah-langkah:

1. Fork repository
2. Buat branch baru

```bash
git checkout -b fitur-baru
```

3. Commit perubahan

```bash
git commit -m "Menambahkan fitur baru"
```

4. Push ke repository

```bash
git push origin fitur-baru
```

5. Buat Pull Request

---

# 📄 Lisensi

Project ini menggunakan lisensi **MIT License**.

Silakan menggunakan, memodifikasi, dan mendistribusikan project ini sesuai ketentuan lisensi MIT.

---

# 👨‍💻 Author

**Nama:** Nama Anda

**GitHub:** https://github.com/USERNAME

**Email:** email@example.com

---

## ⭐ Jika project ini bermanfaat

Jangan lupa berikan **Star ⭐** pada repository ini agar semakin banyak orang yang dapat memanfaatkannya.

**Terima kasih telah menggunakan KulinerBuddyAI! 🍽🤖**
