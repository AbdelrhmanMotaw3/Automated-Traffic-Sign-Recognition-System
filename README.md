

# 🚦 Automated Traffic Sign Recognition System

A deep learning-based web application that classifies traffic signs from images using a Convolutional Neural Network (CNN). Built with TensorFlow and Streamlit, it provides an intuitive interface for real-time predictions.

---

## 📸 Demo

Try the live app here:  
🔗 [Streamlit App]([https://automated-traffic-sign-recognition-system.streamlit.app/](https://automated-traffic-sign-recognition-system-5dbegjn7biglnjhvtv9t.streamlit.app/))

---

## 📂 Repository Structure

```
├── streamlit_app.py         # Streamlit web application
├── main.ipynb               # Model training and evaluation notebook
├── model.h5                 # Trained CNN model
├── traffic_sign_names.csv   # Mapping of class indices to sign names
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
```

---

## 🧠 Model Architecture

The CNN model classifies traffic signs into 43 categories.

```
Input Layer: 32x32x3 RGB image
↓
Conv2D (32 filters, 3x3) + ReLU
↓
Conv2D (32 filters, 3x3) + ReLU
↓
MaxPooling2D (2x2)
↓
Dropout (0.25)
↓
Flatten
↓
Dense (128 units) + ReLU
↓
Dropout (0.5)
↓
Dense (43 units) + Softmax
```

---

## 🗃️ Dataset

- **Name:** German Traffic Sign Recognition Benchmark (GTSRB)  
- **Classes:** 43  
- **Source:** [GTSRB Dataset][(https://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/data))

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or above

### Installation

```bash
# Clone the repository
git clone https://github.com/AbdelrhmanMotaw3/Automated-Traffic-Sign-Recognition-System.git

# Navigate to the directory
cd Automated-Traffic-Sign-Recognition-System

# Install dependencies
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run streamlit_app.py
```

---

## ✨ Features

- Real-time traffic sign classification
- Simple and responsive UI
- Displays prediction confidence
- Preprocessing and error handling included

---


## 📈 Future Enhancements

- Add data augmentation
- Support more image formats
- Deploy on mobile
- Show prediction explanation (Grad-CAM)

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

- GTSRB Dataset team  
- Streamlit for frontend  
- TensorFlow for deep learning framework
```

---

