import streamlit as st
from rembg import remove
from PIL import Image
import io

# Konfigurasi tampilan halaman
st.set_page_config(page_title="Hapus Background", layout="centered")

# Judul
st.title("🧼 Hapus Background Gambar")

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar...", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Baca file sebagai byte
    input_bytes = uploaded_file.read()

    # Tampilkan gambar asli
    image = Image.open(io.BytesIO(input_bytes))
    st.image(image, caption="Gambar Asli", use_container_width=True)

    # Tombol untuk menghapus background
    if st.button("Hapus Background"):
        # Proses hapus background
        output_bytes = remove(input_bytes)
        output_image = Image.open(io.BytesIO(output_bytes))

        # Tampilkan hasil
        st.image(output_image, caption="Tanpa Background", use_container_width=True)

        # Tombol download hasil
        st.download_button(
            label="⬇️ Download Hasil",
            data=output_bytes,
            file_name="hasil.png",
            mime="image/png"
        )
