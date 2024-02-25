OCR (Optical Character Recognition) App
This is a simple Optical Character Recognition (OCR) application built using Python and Tkinter. The app allows users to select an image file containing text, choose a language, and perform OCR to extract text from the image.

Features
Choose an image file: Users can select an image file from their local system using the file dialog.
Select language: The app supports multiple languages for OCR, including English, Arabic, Spanish, and Urdu.
Perform OCR: Once an image is selected and a language is chosen, users can click the "Perform OCR" button to start the OCR process.
Display OCR result: The extracted text from the image is displayed in a text box within the app interface.
Loading screen: A loading screen is displayed while the OCR process is ongoing to provide feedback to the user.
Getting Started
To run the OCR App:

Clone this repository to your local machine.
Make sure you have Python installed on your system.
Install the required dependencies by running pip install -r requirements.txt.
Run the main.py file using Python.
The OCR App interface will open, allowing you to use the application.
Dependencies
The following dependencies are used in this project:

tkinter: Python's standard GUI (Graphical User Interface) toolkit.
Pillow: Python Imaging Library (PIL), which adds support for opening, manipulating, and saving many different image file formats.
OpenCV: Open Source Computer Vision Library, which provides functions for image processing.
EasyOCR: A Python package for Optical Character Recognition.
ssl: Python's SSL module, used for secure connections.

License
This project is licensed under the GNU General Public License (GPL)
