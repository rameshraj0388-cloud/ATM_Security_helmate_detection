# """
# image, video, camera --> frame --> object detection send
# show the detection result on the frame and in the streamlit app
# """
 
# import os
 
# import cv2
# import numpy as np
# import streamlit as st
# from src.detection_service import DetectionService
# from src.audio_service import AudioService
# from src.utils import get_video_stream
# from tempfile import NamedTemporaryFile
 
 
# detection_service = DetectionService()
# audio_service = AudioService()
 
# st.title("Secure ATM - Helmet Detection App")
# st.write("This app detects whether a person is wearing a helmet or not while entering the ATM premises. If a person is detected with a helmet, an alert sound will be played.")
 
# st.sidebar.title("Input settings")
 
# input_type = st.sidebar.radio("Select input type", ("Image", "Video", "Camera"))
 
 
# def process_image(image):
#     frame, detections_classes = detection_service.detect(image)
#     if "helmet" in detections_classes:
#         audio_service.play_beep()
#     return frame
 
# def process_video(video_file_path):
#     cap = cv2.VideoCapture(video_file_path)
 
#     stframe = st.empty()
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
 
#         frame, detections_classes = detection_service.detect(frame)
#         if "helmet" in detections_classes:
#             audio_service.play_beep()
 
#         stframe.image(frame, channels="BGR", use_column_width=True)
#     cap.release()
 
 
# def process_camera(camera_source):
#     cap = get_video_stream(camera_source)
 
#     stframe = st.empty()
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
 
#         frame, detections_classes = detection_service.detect(frame)
#         if "helmet" in detections_classes:
#             audio_service.play_beep()
 
#         stframe.image(frame, channels="BGR", use_column_width=True)
#     cap.release()
 
 
# # streamlit app logic
# if input_type == "Image":
#     uploaded_file = st.sidebar.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])
#     if uploaded_file is not None:
#         file_bytes = uploaded_file.read()
#         np_array = np.frombuffer(file_bytes, np.uint8)
#         image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
 
#         processed_image = process_image(image)
#         st.image(processed_image, channels="BGR", use_column_width=True)
 
 
# if input_type == "Video":
#     uploaded_file = st.sidebar.file_uploader("Upload a video...", type=["mp4", "avi", "mov"])
#     if uploaded_file is not None:
#         with NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
#             tmp_file.write(uploaded_file.read())
#             video_file_path = tmp_file.name
#         process_video(video_file_path)
#         os.remove(video_file_path)
 
 
# if input_type == "Camera":
#     camera_source = st.sidebar.number_input("Camera source (default is 0)", min_value=0, value=0)
#     process_camera(camera_source)
import os
import cv2
import numpy as np
import streamlit as st

from tempfile import NamedTemporaryFile

from src.detection_service import DetectionService
from src.audio_service import AudioService
from src.utils import get_video_stream

detection_service = DetectionService()
audio_service = AudioService()

st.title("Secure ATM - Helmet Detection App")

st.write(
    """This app detects whether a person is wearing a helmet 
    "or not while entering the ATM premises."""
)

st.sidebar.title("Input settings")

input_type = st.sidebar.radio("Select input type", ("Image", "Video", "Camera"))



def process_image(image):

    frame, detections_classes = detection_service.detect(image)

    # Display status
    if "nohelmet" in detections_classes:
        st.success(" NO HELMET DETECTED")

    elif "helmet" in detections_classes:
        st.error(" HELMET DETECTED")

        # Beep ONLY for helmet
        audio_service.play_beep()

    else:
        st.success("No helmet/head detected")

    return frame


def process_video(video_file_path):
    cap = cv2.VideoCapture(video_file_path)

    stframe = st.empty()
    status_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO detection
        frame, detections_classes = detection_service.detect(frame)

        # Display status
        with status_placeholder.container():
            if "nohelmet" in detections_classes:
                st.success("NO HELMET DETECTED")

            elif "helmet" in detections_classes:
                st.error("HELMET DETECTED")

                # Beep ONLY for helmet
                audio_service.play_beep()

            else:
                st.success("No helmet/head detected")
        # Display video frame
        stframe.image(frame, channels="BGR", width="stretch")

    cap.release()


def process_camera(camera_source):
    cap = get_video_stream(camera_source)
    stframe = st.empty()
    status_placeholder = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error(" Unable to read frame from camera.")
            break

        frame, detections_classes = detection_service.detect(frame)
        with status_placeholder.container():
            # NO HELMET
            if "nohelmet" in detections_classes:
                st.success("NO HELMET DETECTED")
            # HELMET
            elif "helmet" in detections_classes:
                st.error("HELMET DETECTED")
                audio_service.play_beep() # Beep ONLY for helmet
             
            else:   # NOTHING DETECTED
                st.success("No helmet/head detected")
        stframe.image(frame, channels="BGR", width="stretch")
    cap.release()


if input_type == "Image":

    uploaded_file = st.sidebar.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        file_bytes = uploaded_file.read()

        np_array = np.frombuffer(file_bytes, np.uint8)

        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        processed_image = process_image(image)

        st.image(processed_image, channels="BGR", width="stretch")

if input_type == "Video":

    uploaded_file = st.sidebar.file_uploader("Upload a video...", type=["mp4", "avi", "mov"])

    if uploaded_file is not None:

        with NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:

            tmp_file.write(uploaded_file.read())

            video_file_path = tmp_file.name

        process_video(video_file_path)

        os.remove(video_file_path)


if input_type == "Camera":
    camera_source = st.sidebar.number_input("Camera source (default is 0)", min_value=0, value=0, step=1)
    process_camera(camera_source)