import streamlit as st
from PIL import Image
from rembg import remove
import io

# ---- Page Config ----
icon = Image.open("ts.avif")

st.set_page_config(
    page_title="Remove By TS",
    page_icon=icon,
    layout="centered"
)

# ---- Title ----
st.title("🪄 Remove By TS")
st.caption("Upload image → Remove background → Download")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)

    st.subheader("Original Image")
    st.image(img, use_container_width=True)

    if st.button("✨ Remove Background", use_container_width=True):
        with st.spinner("Removing Background..."):

            input_bytes = uploaded_file.getvalue()
            output_bytes = remove(input_bytes)
            output = Image.open(io.BytesIO(output_bytes))

        st.subheader("Background Removed Image")
        st.image(output)

        st.download_button(
            label="⬇️ Download Image",
            data=output_bytes,
            file_name="remove_by_ts.png",
            mime="image/png",
            use_container_width=True
        )

st.divider()

# ---- Social Buttons ----
col1, col2 = st.columns(2)

with col1:
    st.link_button(
        "🐙 GitHub",
        "https://github.com/shubham0182",
        use_container_width=True
    )

with col2:
    st.link_button(
        "📸 Instagram",
        "https://instagram.com/_shubhhh_012",
        use_container_width=True
    )

st.markdown(
    "<center>✨ Created by <b>Mr Shubham</b></center>",
    unsafe_allow_html=True
)
