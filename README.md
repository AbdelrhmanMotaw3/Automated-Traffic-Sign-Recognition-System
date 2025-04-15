
## 🚦 Automated Traffic Sign Recognition System
A deep learning-based web application that classifies traffic signs from images using a Convolutional Neural Network (CNN). Built with TensorFlow and Streamlit, it provides an intuitive interface for real-time predictions

---

### 📸 Demo
Experience the live application her:  
🔗 [Streamlit App]([https://automated-traffic-sign-recognition-system.streamlit.app](https://automated-traffic-sign-recognition-system-5dbegjn7biglnjhvtv9t.streamlit.app/)/)

---

### 📂 Repository Structue



```bash
├── streamlit_app.py         # Streamlit web application
├── main.ipynb               # Model training and evaluation notebook
├── model.h5                 # Trained CNN model
├── traffic_sign_names.csv   # Mapping of class indices to sign names
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
``



---

### 🧠 Model Architectre

The CNN model is designed to efficiently extract features from traffic sign images and classify them into 43 categoies



```text
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
``


### 🗃️ Dataset

- **Nae:** German Traffic Sign Recognition Benchmark (TSRB)
- **Classs:* 43
- **Descriptin:** A comprehensive dataset containing over 50,000 images of traffic signs captured under various condiions.
- **Soure:** [GTSRB Dataset]([https://benchmark.ini.rub.de/?section=gtsrb&subsection=daaset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/data))

---

### 🚀 Getting Started

#### Prerequiites

Ensure you have Python 3.7 or higher insalled.

#### Installtion



```bash
# Clone the repository
git clone https://github.com/AbdelrhmanMotaw3/Automated-Traffic-Sign-Recognition-System.git

# Navigate to the project directory
cd Automated-Traffic-Sign-Recognition-System

# Install dependencies
pip install -r requirements.tx
```



#### Running the Appliction



```bash
# Start the Streamlit app
streamlit run streamlit_app.p
``



Upload a `.png` image of a traffic sign, and the application will display the predicted class along with the confidencescore.

---

### ✨ Featues

- Real-time traffic sign classifcaton
- User-friendly web inerfce
- Displays predicted class name and confidenc leel
- Handles image preprocessing and normalzaton
- Provides informative error messages for unsupportedinputs

---

### 🧑‍💻 Contrbutors

| Name               | Role                             |
|--------------------|----------------------------------|
| Abdelrhman Motawea | Model development & deployment   |
| [Contributor 2]    | Data preprocessing & augmentation|
| [Contributor 3]    | UI/UX design & testing           |
| [Contributor 4]    | Documentation & presentaton     |

---

### 📈 Future Enhancments

- Implement data augmentation for improved model obutness
- Expand support to additional image formats (e.g., PEG BMP)
- Integrate with mobile platforms for on-the-go peditions
- Enhance the UI with detailed prediction exlanations

---

### � License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file fr details.

---

### 🙌 Acknowldgments

- [GTSRB Dataset]([https://benchmark.ini.rub.de/?section=gtsrb&subsection=dataset](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign/data)) for providingthedataset
- [Streamlit](https://streamlit.io/) for the web applicatin famework
- [TensorFlow](https://www.tensorflow.org/) for modeldevelopmnt

---

Feel free to customize this `README.md` further to match any additional specifics of yur project. If you need assistance with creating visual assets like the CNN architecture diagram or sample input/output images, let me know! 
