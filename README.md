# ANRP
AI project

# Automatic Number Plate Recognition (ANPR) System

This project is an Automatic Number Plate Recognition (ANPR) system built using Python, OpenCV, EasyOCR, and Django. It allows for the detection, extraction, and recognition of vehicle number plates from images.

## Features

- Vehicle number plate detection and extraction using computer vision techniques with OpenCV.
- Optical Character Recognition (OCR) for number plate recognition using EasyOCR.
- Support for processing images.
- User-friendly web interface built with Django and HTML for easy interaction with the ANPR system.
- Storage and retrieval of processed number plate data using a backend database.

## Prerequisites

To run the ANPR system, you need to have the following installed:

- Python 3.x
- OpenCV library
- EasyOCR library
- Django framework


## Getting Started

1. Clone the repository to your local machine or download the source code as a ZIP file.

    ```bash
    git clone https://github.com/sameerhussain3211/ANPR.git
    ```
    
2. Navigate to the project directory.

    ```bash
    cd ANRP
    ```
3. Install Prerequisites
    ```bash
    pip install opencv-python
    pip install easyocr
    pip install django
    ```

4. Start the Django development server.
    ```bash
    python manage.py runserver
    ```

5. Access the ANPR system in your web browser.
    ```bash
    http://localhost:8000
    ```
## Usage

1. Upload an image (Sample images are given), write the name of the image in the text Text field.
2. The system will detect and extract number plates from the input.
3. The extracted number plate regions will be sent to EasyOCR for character recognition.
4. Recognized number plate information will be displayed on the web interface.
5. Processed number plate data will be searched in the backend database for a match.
6. If found details will be fetched and displayed
7. You can ass new details to the database

## Acknowledgments

This ANPR system was built using Python, OpenCV, EasyOCR, and Django, incorporating techniques from computer vision and optical character recognition. It was developed as a demonstration project for AI Course, to showcase the capabilities of ANPR technology.

## Author

- SAMEER HUSSAIN
- GitHub: [GitHub Profile](https://github.com/sameerhussain3211)

