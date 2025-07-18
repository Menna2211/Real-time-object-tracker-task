import cv2

def open_webcam(index=0):
    # Open the webcam with the specified index (0 is usually the default webcam)
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        return None
    return cap

def get_initial_frame(cap):
    # Read the first frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to read initial frame from webcam.")
        return None
    return frame

def select_object(frame):
    # Display the frame and allow the user to select a region of interest (ROI)
    window_name = "Select Object"
    bbox = cv2.selectROI(window_name, frame, fromCenter=False, showCrosshair=True)
    cv2.destroyWindow(window_name)
    return bbox

def setup_tracker(frame, bbox):
    # Initialize the CSRT tracker with the selected bounding box
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)
    return tracker

def draw_tracking_box(frame, bbox):
    # Draw the bounding box on the frame
    x, y, w, h = [int(v) for v in bbox]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.putText(frame, "Object Tracking", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

def draw_lost_message(frame):
    # Display a message when the object is lost
    cv2.putText(frame, "Object Lost", (50, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

def track_object(cap, tracker):
    # Continuously read frames from the webcam and update the tracker
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to read frame from webcam.")
            break

        success, bbox = tracker.update(frame)

        if success:
            draw_tracking_box(frame, bbox)
        else:
            draw_lost_message(frame)

        cv2.imshow("Object Tracker", frame)

        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break
