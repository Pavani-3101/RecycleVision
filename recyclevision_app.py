import streamlit as st
import cv2
import numpy as np
from skimage.feature import hog
import joblib

# Load the saved model
model = joblib.load("recyclevision_model.pkl")

st.title("♻️ RecycleVision")
st.write("Upload an image to check if it is **Recyclable** or **Not Recyclable**")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Convert uploaded file to OpenCV format
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img_resized = cv2.resize(img, (64, 64))
    
    # Preprocess for HOG
    gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)
    fd = hog(gray, pixels_per_cell=(8, 8), cells_per_block=(2, 2), visualize=False)
    fd = fd.reshape(1, -1)
    
    # Prediction
    pred = model.predict(fd)[0]
    label = "♻️ Recyclable" if pred == 1 else "🚯 Not Recyclable"
    
    st.image(img, caption="Uploaded Image", use_column_width=True)
    st.success(f"Prediction: {label}")
