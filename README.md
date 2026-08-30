# ATM_Security_helmate_detection
ATM Helmet Detection is an AI security tool using Python, OpenCV, and YOLOv8 to identify people obscuring their faces inside ATM kiosks. It processes live CCTV feeds to detect helmets or masks, logs photographic evidence, and sends real-time webhook alerts to bank security hubs to prevent fraud, theft, and kiosk vandalism.

secure_atm/
│
├── models/
│   └── best.pt                  # YOLOv8 trained model
│
├── src/
│   ├── app.py                   # Main Streamlit app
│   ├── detection_service.py     # YOLO detection logic
│   ├── audio_service.py         # Beep alert service
│   └── utils.py                 # Utility functions
│
├── assets/
│   └── beep.wav                 # Alert sound
│
├── config.py                    # Model path & threshold config
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
