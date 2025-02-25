from stegano import lsb
from Crypto.Cipher import AES
import os
import base64
from tkinter import Tk, filedialog, simpledialog, messagebox
import shutil
import qrcode
from PIL import Image
import cv2

def pad_message(message):
    return message + (16 - len(message) % 16) * " "

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_text = cipher.encrypt(pad_message(message).encode())
    return base64.b64encode(encrypted_text).decode()

def decrypt_message(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_message)).decode().strip()
    return decrypted_text

def hide_data(image_path, message, password, output_path):
    key = password.ljust(16)[:16].encode()
    encrypted_message = encrypt_message(message, key)
    secret_image = lsb.hide(image_path, encrypted_message)
    secret_image.save(output_path)
    print("Data hidden successfully in", output_path)

def extract_data(image_path, password):
    key = password.ljust(16)[:16].encode()
    hidden_message = lsb.reveal(image_path)
    if hidden_message:
        try:
            decrypted_message = decrypt_message(hidden_message, key)
            print("Extracted Message:", decrypted_message)
        except:
            print("Incorrect password or corrupted data!")
    else:
        print("No hidden message found!")

def generate_qr_code(data, output_path):
    qr = qrcode.make(data)
    qr.save(output_path)
    print("QR Code saved at", output_path)

def decode_qr_code(image_path):
    qr_image = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(qr_image)
    if data:
        print("Decoded QR Code Message:", data)
    else:
        print("No QR Code detected or unable to decode!")

def hide_file(image_path, file_path, password, output_path):
    with open(file_path, "rb") as f:
        file_data = base64.b64encode(f.read()).decode()
    hide_data(image_path, file_data, password, output_path)

def extract_file(image_path, password, output_path):
    key = password.ljust(16)[:16].encode()
    hidden_message = lsb.reveal(image_path)
    if hidden_message:
        try:
            decrypted_file_data = base64.b64decode(decrypt_message(hidden_message, key))
            with open(output_path, "wb") as f:
                f.write(decrypted_file_data)
            print("Extracted file saved at", output_path)
        except:
            print("Incorrect password or corrupted data!")
    else:
        print("No hidden file found!")

if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    
    choice = simpledialog.askinteger("Steganography", "Select an option:\n1. Hide Data\n2. Reveal Data\n3. Hide File\n4. Extract File\n5. Generate QR Code\n6. Decode QR Code")
    
    if choice == 1:
        image_path = filedialog.askopenfilename(title="Select Image for Hiding Data", filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        message = simpledialog.askstring("Input", "Enter the secret message:")
        password = simpledialog.askstring("Input", "Enter a password:", show="*")
        output_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Image")
        hide_data(image_path, message, password, output_path)
        messagebox.showinfo("Success", "Data hidden successfully!")
    elif choice == 2:
        image_path = filedialog.askopenfilename(title="Select Image to Extract Data", filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        password = simpledialog.askstring("Input", "Enter the password:", show="*")
        extract_data(image_path, password)
    elif choice == 3:
        image_path = filedialog.askopenfilename(title="Select Image for Hiding File", filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        file_path = filedialog.askopenfilename(title="Select File to Hide")
        password = simpledialog.askstring("Input", "Enter a password:", show="*")
        output_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Image")
        hide_file(image_path, file_path, password, output_path)
        messagebox.showinfo("Success", "File hidden successfully!")
    elif choice == 4:
        image_path = filedialog.askopenfilename(title="Select Image to Extract File", filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        password = simpledialog.askstring("Input", "Enter the password:", show="*")
        output_path = filedialog.asksaveasfilename(title="Save Extracted File")
        extract_file(image_path, password, output_path)
    elif choice == 5:
        data = simpledialog.askstring("Input", "Enter data for QR Code:")
        output_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save QR Code")
        generate_qr_code(data, output_path)
        messagebox.showinfo("Success", "QR Code generated successfully!")
    elif choice == 6:
        image_path = filedialog.askopenfilename(title="Select QR Code Image", filetypes=[("Image Files", "*.png;*.jpg;*.bmp")])
        decode_qr_code(image_path)
    else:
        print("Invalid choice!")
