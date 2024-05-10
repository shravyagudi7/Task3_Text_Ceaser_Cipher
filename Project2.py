import tkinter as tk
from tkinter import messagebox

# Function to perform Caesar encryption
def encrypt_message():
    try:
        shift = int(entry_shift.get())
        message = entry_message.get()
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
                encrypted_message += shifted_char
            else:
                encrypted_message += char
        result_label.config(text=f'Encrypted Message: {encrypted_message}')
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")

# Function to perform Caesar decryption
def decrypt_message():
    try:
        shift = int(entry_shift.get())
        message = entry_message.get()
        decrypted_message = ''
        for char in message:
            if char.isalpha():
                shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
                decrypted_message += shifted_char
            else:
                decrypted_message += char
        result_label.config(text=f'Decrypted Message: {decrypted_message}')
    except ValueError:
        messagebox.showerror("Error", "Shift value must be an integer.")

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher Encryption/Decryption")
window.configure(bg='#f0f0f0')

# Create and configure widgets
label_message = tk.Label(window, text="Enter Message:", font=("Arial", 14), bg='#f0f0f0')
label_shift = tk.Label(window, text="Enter Shift:", font=("Arial", 14), bg='#f0f0f0')
entry_message = tk.Entry(window, font=("Arial", 14))
entry_shift = tk.Entry(window, font=("Arial", 14))
encrypt_button = tk.Button(window, text="Encrypt", font=("Arial", 14), command=encrypt_message, bg='#4CAF50', fg='white')
decrypt_button = tk.Button(window, text="Decrypt", font=("Arial", 14), command=decrypt_message, bg='#2196F3', fg='white')
result_label = tk.Label(window, text="", font=("Arial", 14), wraplength=300, justify="center", bg='#f0f0f0')

# Place widgets in the window
label_message.pack(pady=(20, 5))
entry_message.pack(pady=5, padx=20, ipadx=20)
label_shift.pack(pady=(5, 5))
entry_shift.pack(pady=5, padx=20, ipadx=20)
encrypt_button.pack(pady=(10, 10), padx=20, ipadx=10)
decrypt_button.pack(pady=(10, 20), padx=20, ipadx=10)
result_label.pack(pady=(0, 20))

# Start the GUI application
window.mainloop()
