import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the model (cached so it doesn't reload every time)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(r"F:\DEPI Microsoft Machine Learning\Round2\GP\EDA for 1st Milestone\model.h5")
    return model

# Function to prepare and preprocess the image before feeding it to the model
def prepare_image(img):
    img = img.resize((32, 32))  
    img_array = np.array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add an extra dimension for batch size
    img_array = img_array / 255.0  # Normalize the image data
    return img_array

# Streamlit page configuration
st.set_page_config(page_title="Traffic Sign Recognition", page_icon="🚦", layout="wide")  # Custom page settings
st.title("Automated Traffic Sign Recognition 🚦")
st.write("Upload a PNG image of a traffic sign, and I’ll predict the class and confidence.")

# Sidebar with helpful information
st.sidebar.title("Options")
st.sidebar.markdown("""
This application allows you to upload a traffic sign image, and it will predict the sign’s class and confidence level.
Upload a PNG image, and see the result!
""")

# File uploader widget
uploaded_file = st.file_uploader("Choose a PNG image...", type="png")

if uploaded_file is not None:
    # Open the image
    img = Image.open(uploaded_file)
    
    # Display the image neatly
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Prepare image data for prediction
    img_array = prepare_image(img)
    
    # Load model and predict
    model = load_model()
    prediction = model.predict(img_array)
    predicted_class = prediction.argmax()
    confidence = prediction.max()

    # Display predicted class with a background color and border
    st.markdown(f"""
    <div style="background-color: #f7f7f7; border: 2px solid #2196F3; padding: 10px; border-radius: 8px;">
        <h3 style="color: #2196F3;">Predicted Class: <strong>{predicted_class}</strong></h3>
    </div>
    """, unsafe_allow_html=True)

    # Display confidence with a background color and border
    st.markdown(f"""
    <div style="background-color: #e8f5e9; border: 2px solid #388E3C; padding: 10px; border-radius: 8px;">
        <h3 style="color: #388E3C;">Confidence: <strong>{confidence * 100:.2f}%</strong></h3>
    </div>
    """, unsafe_allow_html=True)
