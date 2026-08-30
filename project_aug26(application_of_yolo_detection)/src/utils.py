import cv2

def get_video_stream(camera_source):
    cap = cv2.VideoCapture(camera_source)

    if not cap.isOpened():
        print(f"Error: Could not open camera source {camera_source}")
        return None
    return cap

def release_video_stream(cap):
    cap.release()