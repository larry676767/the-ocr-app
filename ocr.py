import tkinter as tk
from tkinter import ttk, filedialog
import cv2
from PIL import Image, ImageTk
import easyocr
import ssl
import threading

class LoadingScreen:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.title("Loading")
        self.root.geometry("200x100")
        self.label = tk.Label(self.root, text="Performing OCR...", font=("Helvetica", 12))
        self.label.pack(pady=20)
        self.progressbar = ttk.Progressbar(self.root, mode='indeterminate')
        self.progressbar.pack(pady=10)
        self.progressbar.start()

    def close(self):
        self.root.destroy()

class OCRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR App")
        self.image = None
        self.tk_image = None
        self.language = tk.StringVar()
        self.language.set("English")  # Default language
        self.create_widgets()

    def create_widgets(self):
        self.language_label = tk.Label(self.root, text="Select Language:")
        self.language_label.grid(row=0, column=0, padx=10, pady=10)
        self.language_dropdown = tk.OptionMenu(self.root, self.language, "English", "Arabic", "Spanish", "Urdu")
        self.language_dropdown.grid(row=0, column=1, padx=10, pady=10)
        self.choose_button = tk.Button(self.root, text="Choose Image", command=self.choose_image)
        self.choose_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        self.image_label = tk.Label(self.root)
        self.image_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.ocr_button = tk.Button(self.root, text="Perform OCR", command=self.start_ocr_process)
        self.ocr_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.result_text = tk.Text(self.root, height=10, width=50)
        self.result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def choose_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.display_image()

    def display_image(self):
        if self.image is not None:
            image_rgb = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
            image_pil = Image.fromarray(image_rgb)
            width, height = image_pil.size
            if width > 640 or height > 480:
                image_pil.thumbnail((640, 480))
            self.tk_image = ImageTk.PhotoImage(image_pil)
            self.image_label.config(image=self.tk_image)

    def start_ocr_process(self):
        if self.image is not None:
            loading_screen = LoadingScreen()
            ocr_thread = threading.Thread(target=self.perform_ocr, args=(loading_screen,))
            ocr_thread.start()

    def perform_ocr(self, loading_screen):
        selected_language = self.language.get()
        languages_mapping = {"English": "en", "Arabic": "ar", "Spanish": "es", "Urdu": "ur"}
        selected_language_code = languages_mapping.get(selected_language)
        if selected_language_code:
            reader = easyocr.Reader([selected_language_code])
            result = reader.readtext(self.image)
            loading_screen.close()
            self.display_ocr_result(result)

    def display_ocr_result(self, result):
        self.result_text.delete(1.0, tk.END)
        for detection in result:
            self.result_text.insert(tk.END, detection[1] + "\n")

def main():
    # Disable SSL certificate verification
    ssl._create_default_https_context = ssl._create_unverified_context
    root = tk.Tk()
    app = OCRApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
