# Secure Data Hiding in Images Using Steganography  

## 📌 Project Overview  
This project implements **image steganography** using **Least Significant Bit (LSB) encoding** to securely hide text messages and files within images. It also includes **AES encryption** for enhanced security and supports **QR code encoding/decoding** for added functionality.  

## 🚀 Features  
✅ **Text & File Steganography** – Hide both **text messages and entire files (PDF, TXT, etc.)** inside images.  
✅ **AES Encryption** – Encrypt hidden messages for added security.  
✅ **QR Code Integration** – Encode messages into QR codes and extract hidden data from them.  
✅ **Drag-and-Drop Support** – Easily select images and files using a **user-friendly GUI**.  
✅ **Cross-Platform Compatibility** – Works seamlessly on **Windows and Linux**.  
✅ **Multiple Image Format Support** – Works with **PNG, JPG, BMP** formats.  
✅ **Minimal Image Distortion** – Ensures that the hidden data does not alter the visible quality of the image.  

## 🛠️ Technologies Used  

### **Libraries & Tools**  
- **Python** – Main programming language for implementation.  
- **OpenCV** – For image processing and manipulation.  
- **Stegano** – Python library for LSB steganography.  
- **NumPy** – Efficient handling of image arrays.  
- **PyCryptodome** – AES encryption for secure data hiding.  
- **qrcode** – QR code generation and decoding.  
- **Tkinter** – GUI for file selection and input.  

### **Platforms**  
- **Linux/Windows** – Works across multiple operating systems.  
- **VS Code** – Used for writing and debugging code.  
- **GitHub** – Version control and project sharing.  


## 🔧 Installation & Usage  

### **1️⃣ Install Required Libraries**  
pip install opencv-python numpy stegano pycryptodome qrcode pillow tk
2️⃣ Run the Application
bash
Copy
Edit
python steg.py
3️⃣ Select an Option
Hide a Message – Choose an image, enter a message or select a file, and save the output.
Extract a Message – Select a stego image to reveal the hidden content.
QR Code Mode – Encode a message into a QR code or extract hidden text from an existing QR code.
🔮 Future Scope
Multi-layered Steganography – Hiding data across multiple image layers.
Video & Audio Steganography – Extending support beyond images.
AI-based Steganalysis Resistance – Making detection even more difficult.
📌 GitHub Repository
🔗 Click Here to View the Repository
