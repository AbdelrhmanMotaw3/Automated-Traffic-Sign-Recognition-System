import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Dictionary mapping class indices to traffic sign descriptions
class_descriptions = {
    0: "Speed limit (20km/h)",
    1: "Speed limit (30km/h)",
    2: "Speed limit (50km/h)",
    3: "Speed limit (60km/h)",
    4: "Speed limit (70km/h)",
    5: "Speed limit (80km/h)",
    6: "End of speed limit (80km/h)",
    7: "Speed limit (100km/h)",
    8: "Speed limit (120km/h)",
    9: "No passing",
    10: "No passing for vehicles over 3.5 metric tons",
    11: "Right-of-way at the next intersection",
    12: "Priority road",
    13: "Yield",
    14: "Stop",
    15: "No vehicles",
    16: "Vehicles over 3.5 metric tons prohibited",
    17: "No entry",
    18: "General caution",
    19: "Dangerous curve to the left",
    20: "Dangerous curve to the right",
    21: "Double curve",
    22: "Bumpy road",
    23: "Slippery road",
    24: "Road narrows on the right",
    25: "Road work",
    26: "Traffic signals",
    27: "Pedestrians",
    28: "Children crossing",
    29: "Bicycles crossing",
    30: "Beware of ice/snow",
    31: "Wild animals crossing",
    32: "End of all speed and passing limits",
    33: "Turn right ahead",
    34: "Turn left ahead",
    35: "Ahead only",
    36: "Go straight or right",
    37: "Go straight or left",
    38: "Keep right",
    39: "Keep left",
    40: "Roundabout mandatory",
    41: "End of no passing",
    42: "End of no passing by vehicles over 3.5 metric tons"
}

# Load the model (cached so it doesn't reload every time)
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model.h5")
    return model

# Function to prepare and preprocess the image before feeding it to the model
def prepare_image(img):
    img = img.resize((32, 32))  
    img_array = np.array(img)  
    img_array = np.expand_dims(img_array, axis=0)  
    img_array = img_array / 255.0  
    return img_array

# Streamlit page configuration
st.set_page_config(page_title="Traffic Sign Recognition", page_icon="🚦", layout="wide")
st.title("Automated Traffic Sign Recognition 🚦")
st.write("Upload a PNG image of a traffic sign, and I’ll predict the class and confidence.")

# Sidebar
st.sidebar.title("Options")
st.sidebar.markdown("""
This application allows you to upload a traffic sign image, and it will predict the sign’s class and confidence level.
Upload a PNG image, and see the result!
""")

# File uploader
uploaded_file = st.file_uploader("Choose a PNG image...", type="png")

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img_array = prepare_image(img)
    model = load_model()
    prediction = model.predict(img_array)
    predicted_class = prediction.argmax()
    confidence = prediction.max()
    description = class_descriptions.get(predicted_class, "Description not available")

    st.markdown(f"""
    <div style="background-color: #f7f7f7; border: 2px solid #2196F3; padding: 10px; border-radius: 8px;">
        <h3 style="color: #2196F3;">Predicted Class: <strong>{predicted_class}</strong> - {description}</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background-color: #e8f5e9; border: 2px solid #388E3C; padding: 10px; border-radius: 8px;">
        <h3 style="color: #388E3C;">Confidence: <strong>{confidence * 100:.2f}%</strong></h3>
    </div>
    """, unsafe_allow_html=True)
