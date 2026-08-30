# ATM_Security_helmate_detection
ATM Helmet Detection is an AI security tool using Python, OpenCV, and YOLOv8 to identify people obscuring their faces inside ATM kiosks. It processes live CCTV feeds to detect helmets or masks, logs photographic evidence, and sends real-time webhook alerts to bank security hubs to prevent fraud, theft, and kiosk vandalism.


## 📂 Project Structure

```text
secure_atm/
│
├── models/
│   └── best.pt                  # YOLOv8 custom-trained model weights
│
├── src/
│   ├── detection_service.py     # Core YOLO object detection logic loop
│   ├── audio_service.py         # Asynchronous beep alert audio handler
│   └── utils.py                 # Core utility helper functions
│
├── assets/
│   └── beep.wav                 # Audio file for security warning alerts
│
├── app.py                       # Main Streamlit dashboard application
├── config.py                    # Global model parameters & threshold settings
├── requirements.txt             # Text log file containing external packages
├── .gitignore                   # Specific folders to ignore in version control
└── README.md                    # Primary repository system documentation
```

# Secure ATM - Helmet Detection App 🏦🪖

A real-time helmet detection system built with **YOLOv8** and **Streamlit** to enhance ATM security premises by triggering immediate audio alerts upon violation detection.

---

## 📋 Project Structure

```text
secure_atm/
│
├── models/
│   └── best.pt                  # YOLOv8 trained model weights
│
├── src/
│   ├── app.py                   # Main Streamlit dashboard application
│   ├── detection_service.py     # YOLO computer vision detection logic
│   ├── audio_service.py         # Beep alert audio loop management
│   └── utils.py                 # Core utility helper functions
│
├── assets/
│   └── beep.wav                 # Warning alert sound asset
│
├── config.py                    # Model paths and confidence threshold configs
├── requirements.txt             # Project external dependencies
├── .gitignore                   # Git version control exclusion file
└── README.md                    # Project documentation front page
```

---

## 🚀 Features

- 📸 **Image Detection** — Upload static images to instantly evaluate helmet/no-helmet compliance.
- 🎥 **Video Detection** — Process uploaded video feeds for frame-by-frame violation auditing.
- 📷 **Camera Detection** — Run live, real-time computer vision inference using a connected webcam.
- 🔊 **Audio Alert** — Plays a warning beep sound 3 times sequentially when a helmet is flagged.
- 🎯 **YOLOv8 Core** — Integrated custom-trained lightweight object detection pipeline.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/sujankim/secure_atm.git
cd secure_atm
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```
* **Windows Activation:** `.venv\Scripts\activate`
* **Mac/Linux Activation:** `source .venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Your Trained Model weights
Ensure your custom-trained weights file is placed inside the dedicated subfolder:
`secure_atm/models/best.pt`

### 5. Launch the Dashboard app
```bash
streamlit run src/app.py
```

---

## 🧠 Model Details

| Property | Value |
| :--- | :--- |
| **Model Architecture** | YOLOv8n (Nano) |
| **Target Classes** | `nohelmet`, `helmet` |
| **Training Dataset Size** | 113 Images |
| **Validation Dataset Size** | 12 Images |
| **Overall mAP50** | 0.919 |
| **Helmet Class mAP50** | 0.964 |
| **No Helmet Class mAP50**| 0.875 |
| **Training Epochs** | 100 |
| **Native Image Resolution**| 640 × 640 pixels |

---

## 📦 Core Dependencies

- **Streamlit** (Interactive Dashboard Web Interface)
- **Ultralytics YOLOv8** (Deep Learning Object Inference)
- **OpenCV** & **NumPy** (Image Preprocessing & Array Transformations)
- **playsound3** & **SciPy** (Audio Alert Management Engine)

---

## 🙏 Acknowledgements

A special thanks to our instructor **Gangan Puri** for his continuous guidance, support, and mentorship throughout this project. We are also incredibly grateful to him for providing the specialized helmet detection dataset used to train our core YOLOv8 model. 

*"Thank you for making Computer Vision approachable and practical for us."*

---

## 👥 Project Team

- **kartik kushawaha** — Primary System Developer
- **Gangan Puri** — Project Instructor & Advisor

[![**Gangan Puri**](https://shields.io)](https://www.linkedin.com/in/puri-gagan)


---

## 📝 License
This project is built strictly for educational purposes only.

