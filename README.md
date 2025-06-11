# QR Code Project

This project includes three files:

1. **QR-Code Detector Live.py** 
   This file detects QR codes in real-time using your webcam. It draws a rectangle around the detected QR code, displays its data above it, prints the data in the console, and copies it to the clipboard.  
   ⚠️ **Don't forget to allow webcam access.**

2. **QR-Code Maker.py**  
   This file receives text input from the console, generates a QR code with that data, saves the QR code image, and displays it.

3. **QR-Code Detector From Pic.py**  
   This file loads an image named `qrcode.png`, detects any QR codes in it, draws a rectangle around them, writes the data above the rectangl, and saves the result.  
   ⚠️ **Don't forget to rename your image to `qrcode.png`.**


### 📦 Requirements:
- Python 3  
- OpenCV (`cv2`)  
- Pyzbar  
- os (standard library)  
- pyperclip 
