import streamlit as st

st.set_page_config(
    page_title="KulinerBuddy AI",
    page_icon="🍳",
    layout="wide"
)

# Header
col1, col2 = st.columns([1,5])

with col1:
    st.image("culinerbuddyai.png", width=80)

with col2:
    st.title("KulinerBuddy AI")
    st.caption("Your personal culinary buddy")

st.divider()

# Chat
with st.chat_message("assistant"):
    st.write("👋 Hi! I'm **KulinerBuddy AI**.")
    st.write("What can I cook for you today?")

with st.chat_message("user"):
    st.write("Aku lagi pengen makan yang pedas tapi gampang dibuat, ada rekomendasi?")

with st.chat_message("assistant"):
    st.write("🔥 Siap! Ini beberapa rekomendasi menu pedas yang mudah dibuat.")

st.subheader("🍽️ Rekomendasi Untukmu")

col1, col2, col3 = st.columns(3)

with col1:
    st.image("https://picsum.photos/300/200?1")
    st.write("### Ayam Geprek")
    st.caption("20 menit")

with col2:
    st.image("https://picsum.photos/300/200?2")
    st.write("### Mie Goreng Pedas")
    st.caption("15 menit")

with col3:
    st.image("https://picsum.photos/300/200?3")
    st.write("### Tahu Cabe Garam")
    st.caption("15 menit")

st.divider()

prompt = st.chat_input("Ketik pesan...")
