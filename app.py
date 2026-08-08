import streamlit as st
import time
import os
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Happy Birthday Vijay!",
    page_icon="🎂",
    layout="centered"
)

# Balloons animation when page opens
st.balloons()

# Header
st.title("🎉 Happy Birthday, Vijay! 🎂")
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

# Photo Gallery Section
st.subheader("📸 Memories & Good Times")

# Searches the current root directory (works both locally AND on Streamlit Cloud!)
folder_path = "."

valid_extensions = ('.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG')
image_files = [f for f in os.listdir(folder_path) if f.endswith(valid_extensions)]

if image_files:
    for img_file in image_files:
        try:
            image = Image.open(img_file)
            st.image(image, caption=f"Memory: {img_file}", width="stretch")
        except Exception as e:
            st.error(f"Could not load image {img_file}: {e}")
else:
    st.info("No images uploaded yet.")

st.divider()
st.caption("Designed with ❤️ using Python & Streamlit")
