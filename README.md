# 👐 HandTracking using MediaPipe and OpenCV

This repository contains a Python script for hand tracking using MediaPipe and OpenCV. It utilizes the MediaPipe library to detect and track hands in a live webcam feed, drawing landmarks and connections on the detected hands.

## 🛠️ Requirements

- Python 3.x 🐍
- OpenCV (`cv2`) 📷
- MediaPipe (`mediapipe`) 🎥

## ⬇️ Installation

To install the required libraries, run the following command:

```
pip install opencv-python mediapipe
```

## 🚀 Usage 

1. Clone this repository or download the `HandTracking.py` script.

2. Run the script using the following command:

```
python HandTracking.py
```

3. Once the script is running, it will open your webcam feed and start detecting and tracking your hands.

4. You'll see landmarks and connections drawn on your hands in real-time.

5. Press the 'Esc' key to exit the program.

## ✨ Features

- Detects and tracks multiple hands in a webcam feed.
- Draws landmarks and connections on the detected hands for visualization.
- Calculates and displays the frame rate (FPS) of the webcam feed.

## 🔧 Customization 

You can import the  HandTrackingModule.py script and customize the behavior of the hand detector by modifying the parameters in the handDetector class constructor of the script. Here are some parameters you can adjust:

- `mode`: Set to `True` if using static images (default is `False` for webcam feed).
- `maxHands`: Maximum number of hands to detect (default is `2`).
- `detectionCon`: Minimum confidence threshold for hand detection (default is `0.5`).
- `trackCon`: Minimum confidence threshold for hand tracking (default is `0.5`).

You can also modify the drawing specifications (e.g., colors, thickness) by editing the `findHands()` and `findPosition()` methods in the `handDetector` class.

## 🙏 Credits 

This script utilizes the following libraries:

- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library
- [MediaPipe](https://google.github.io/mediapipe/) - A cross-platform framework for building multimodal applied ML pipelines

Special thanks to [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/@murtazasworkshop) for their valuable tutorials and resources in the field of Robotics and AI.

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
