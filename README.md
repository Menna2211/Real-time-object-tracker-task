# Real-Time Object Tracker

A Python application that lets you select an object in the first frame and track it in real time using your webcam. Built with OpenCV's CSRT tracker.

## Project Structure

```
object-tracker/
├── main.py              # Entry point to run the tracker
├── requirements.txt     # Required Python packages
├── README.md            # Project documentation
└── src/
    └── tracker_utils.py # Utility functions: webcam handling, ROI selection, tracker setup, drawing utilities
```

## Features

- Select an object in the first frame
- Real-time object tracking via webcam
- Visual tracking feedback

## Requirements

- Python 3.10+
- OpenCV (cv2)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## How It Works

1. A window opens showing your webcam feed.
2. Use your mouse to draw a rectangle around the object you want to track.
3. Press ENTER or SPACE to confirm your selection.
4. Watch as the tracker follows the object in real time.
5. Press ESC to exit.

## Future Enhancements

- Add object detection (e.g., YOLO) to automatically detect and track objects.