import streamlit as st
import cv2
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim

st.title("🧾 Fake Currency Detection System")

# Step 1: Upload an image
uploaded_file = st.file_uploader("Upload a currency image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Optional: Save or process image
    # e.g., cv2.imwrite("input.jpg", cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR))

    st.write("Analyzing image...")

    # --- Insert processing code from controller.ipynb ---
    # For example, call your functions to:
    # - extract features
    # - compare with reference
    # - calculate SSIM
    # - output results

    # Dummy result:
    st.success("9/10 features matched. Currency likely genuine.")

    # Optional: display individual feature comparisons
    st.image(image_np, caption="Feature X", width=200)
