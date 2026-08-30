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
│   ├── app.py                   # Main Streamlit dashboard application
│   ├── detection_service.py     # Core YOLO object detection logic loop
│   ├── audio_service.py         # Asynchronous beep alert audio handler
│   └── utils.py                 # Core utility helper functions
│
├── assets/
│   └── beep.wav                 # Audio file for security warning alerts
│
├── config.py                    # Global model parameters & threshold settings
├── requirements.txt             # Text log file containing external packages
├── .gitignore                   # Specific folders to ignore in version control
└── README.md                    # Primary repository system documentation
```
