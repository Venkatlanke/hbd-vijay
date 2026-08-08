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
    > **Happiest Birthday, brooo!** 🥳🎂
    >
    > You're in your final year of M.Tech now, and this is just the launchpad for massive things ahead! May you crush your remaining M.Tech semesters, get all your research papers accepted without endless revisions, and turn that big dream of pursuing a Ph.D. in the USA into reality! 🎓🇺🇸🚀
    >
    > May your Python code compile on the first try, your datasets never corrupt, and... most importantly, **may you finally find a partner who can actually survive listening to all your endless research talks without falling asleep!** 😂❤️ *(Or at least someone who pretends your algorithms are fascinating! 🤫)*
    >
    > Keep grinding, keep dreaming big, and keep leveling up. One day, we’ll all be pointing at you and proudly flexing: **“Yep, that’s Professor Vijay right there!”** 😎👨‍🏫
    >
    > Have an incredible day and an unforgettable year ahead, bro! 🎂✨
    """)
    st.snow()

st.divider()

# Photo Gallery Section (Cloud & Local Compatible)
st.subheader("📸 Memories & Good Times")

# Looks inside the GitHub root folder where images are uploaded
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
    st.info("No images uploaded yet. Upload your photos to GitHub to display them here!")

st.divider()
st.caption("Designed with ❤️ using Python & Streamlit")
