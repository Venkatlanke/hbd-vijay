import streamlit as st
import time
import os
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday VijayKedhar!",
    page_icon="🎂",
    layout="centered"
)

# Balloons animation when page opens
st.balloons()

# Header
st.title("🎉 Happy Birthday, VijayKedhar! 🎂")
st.write("### *Built entirely in Python, just for you!*")
st.divider()

# Interactive Secret Surprise Box
st.subheader("🎁 Unlock Your Birthday Message")
if st.button("Click to Open Your Surprise"):
    with st.spinner("Compiling birthday magic..."):
        time.sleep(1.5)
    st.success("Access Granted!")
    
    st.markdown("""
    > ### 🎈 Dear Vijay,
    > Happy Birthday brooo..! From cracking your M.Tech to making your dream of a Ph.D. in the USA a reality, I know you're going to achieve it all.
    > 
    > May your research papers get accepted, your code compile error-free, and your journey to becoming 'Professor Vijay' be smooth and successful! Keep shining and pushing forward! 🎓🇺🇸🚀
    """)
    st.snow()

st.divider()

# Photo Gallery Section for Multiple Images
st.subheader("📸 Memories & Good Times")

folder_path = r"C:\Python\hbdvijay"

# Find all image files in the folder (.png, .jpg, .jpeg)
valid_extensions = ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')
image_files = [f for f in os.listdir(folder_path) if f.endswith(valid_extensions)] if os.path.exists(folder_path) else []

if image_files:
    for img_file in image_files:
        full_img_path = os.path.join(folder_path, img_file)
        try:
            image = Image.open(full_img_path)
            st.image(image, caption=f"Memory: {img_file}", width="stretch")
        except Exception as e:
            st.error(f"Could not load image {img_file}: {e}")
else:
    st.info("No images found in C:\\Python\\hbdvijay folder.")

st.divider()
st.caption("Designed with ❤️ using Python & Streamlit")