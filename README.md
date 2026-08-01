# 🍲 KulinerBuddyAI — Smart Culinary & Dining Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Prototype-orange.svg)]()

**KulinerBuddyAI** adalah asisten pribadi cerdas berbasis Kecerdasan Buatan (AI) yang dirancang untuk membantu pengguna mengatasi kebingungan dalam memilih menu makanan, menemukan kuliner khas lokal, serta mendapatkan rekomendasi tempat makan terbaik yang disesuaikan dengan preferensi pribadi.

---

## 📑 Daftar Isi
- [Latar Belakang](#-latar-belakang)
- [Target Pengguna](#-target-pengguna)
- [Fitur Utama](#-fitur-utama)
- [Arsitektur & Teknologi](#-arsitektur--teknologi)
- [Tampilan Antarmuka (UI)](#-tampilan-antarmuka-ui)
- [Cara Memulai / Instalasi](#-cara-memulai--instalasi)
- [Rencana Pengembangan (Roadmap)](#-rencana-pengembangan-roadmap)
- [Lisensi](#-lisensi)

---

## 💡 Latar Belakang

Seringkali masyarakat atau wisatawan menghabiskan banyak waktu hanya untuk memutuskan *"Mau makan apa hari ini?"* atau kesulitan menemukan tempat makan yang sesuai dengan kriteria diet khusus (seperti Halal atau Vegetarian) di area baru. **KulinerBuddyAI** hadir sebagai solusi serba ada yang memberikan rekomendasi instan, relevan, dan terpersonalisasi secara interaktif melalui percakapan wajar (*Natural Language Processing*).

---

## 🎯 Target Pengguna

1. **Wisatawan & Turis (Lokal/Mancanegara):** Membantu menemukan makanan khas lokal (*authentic local food*) yang populer atau *hidden gem*.
2. **Pecinta Kuliner (*Foodies*):** Mengatur pencarian berdasarkan ulasan tertinggi, suasana tempat makan, dan variasi menu baru.
3. **Masyarakat Umum, Pekerja, & Mahasiswa:** Solusi cepat untuk menentukan menu makan harian berbasis anggaran (*budget-friendly*) dan lokasi terdekat.
4. **Pengguna dengan Kebutuhan Diet Khusus:** Menyediakan filter ketat untuk kriteria **Halal**, pilihan **Vegetarian/Vegan**, serta opsi bebas alergen.

---

## ✨ Fitur Utama

- 📍 **Rekomendasi Berbasis Lokasi & Budget:** Menampilkan opsi tempat makan terdekat lengkap dengan estimasi harga per porsi.
- 🥗 **Filter Kebutuhan Khusus:** Pencarian spesifik untuk menu Halal, Vegetarian, *Child-Friendly*, atau *Open 24 Hours*.
- 🎲 **Fitur *"Bingung Makan Apa"*:** Penentu keputusan acak (*random menu generator*) untuk pengguna yang ragu-ragu.
- 🗺️ **Integrasi Navigasi & Ulasan:** Menyediakan ringkasan rating ulasan dan tautan langsung ke rute navigasi (Google Maps).
- 💬 **Interaksi Percakapan Alami:** Mampu memahami konteks teks seperti *"Cari makan siang pedas di bawah 20 ribu"*.

---

## 🛠️ Arsitektur & Teknologi

- **Bahasa Pemrograman:** Python 3.9+
- **Framework Bot / UI:** Streamlit / Telegram Bot API / Dialogflow *(pilih yang sesuai)*
- **Model AI/LLM:** OpenAI GPT / Google Gemini API / Natural Language Processing (NLP)
- **Database / API:** Google Maps Places API, Database Kuliner Lokal

---

## 🎨 Tampilan Antarmuka (UI)

| Welcoming Screen | Rekomendasi Chatbot | Detail & Rute Lokasi |
| :---: | :---: | :---: |
| *![Tampilan UI Chatbot](LINK_GAMBAR_YANG_ANDA_COPY_TADI)* | *(Unggah Foto UI 2)* | *(Unggah Foto UI 3)* |

*(Catatan: Tangkapan layar UI lengkap dan rancangan wireframe dapat dilihat pada lampiran dokumen PDF proyek)*

---

## 🚀 Cara Memulai / Instalasi

### Prasyarat
- Python 3.9 atau versi yang lebih baru
- Git
- API Key (misal: OpenAI / Gemini / Google Maps API)

### Langkah Instalasi

1. **Clone repository ini:**
   ```bash
   git clone [https://github.com/USERNAME-ANDA/KulinerBuddyAI.git](https://github.com/USERNAME-ANDA/KulinerBuddyAI.git)
   cd KulinerBuddyAI
   python -m venv venv
# Di Windows:
venv\Scripts\activate
# Di macOS/Linux:
source venv/bin/activate
Bash

pip install -r requirements.txt
Code snippet

API_KEY=masukkan_api_key_anda_di_sini
Bash

python main.py
