import steamlit as st
import os
from PIL import Image
from rembg import remove


st.title("Remove Background from Image")
uploded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"], key="file_uploader")


if uploded_file :
    img = Image.open(uploded_file)

    st.subheader("Original Image")
    st.image(img,use_container_width=True)
    if st.button("Rmove Background"):
        with st.spinner("Removing background..."):
            output = remove(img)
        st.subheader("Image with Background Removed")
        st.image(output,use_container_width=True)