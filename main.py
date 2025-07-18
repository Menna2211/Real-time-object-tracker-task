from src.tracker_utils import *

def main():
    """Main function to run the object tracking application."""
    # Open the webcam
    cap = open_webcam()
    if cap is None:
        return
    # Get the initial frame
    first_frame = get_initial_frame(cap)
    if first_frame is None:
        cap.release()
        return
    
    # Select the object to track
    bbox = select_object(first_frame)
    if bbox == (0, 0, 0, 0):
        print("No object selected.")
        cap.release()
        return
    # Setup the tracker
    tracker = setup_tracker(first_frame, bbox)
    track_object(cap, tracker)
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
