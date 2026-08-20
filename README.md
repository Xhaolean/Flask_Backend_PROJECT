# Android & Web to Flask Backend Integration (ExpressIt)

![Android](https://img.shields.io/badge/Platform-Android-green?style=flat&logo=android)
![Python](https://img.shields.io/badge/Backend-Flask-blue?style=flat&logo=flask)
[![Download APK](https://img.shields.io/badge/Download-APK-brightgreen?style=for-the-badge&logo=android)](https://github.com/Xhaolean/Flask_Backend_PROJECT/releases/tag/Feedback)

## About The Project
This open-source project demonstrates how to connect front-end applications—specifically an Android app built with Kotlin and a standard HTML/JS website—to a Python backend. It is designed to help beginners understand how backend REST APIs work, how to handle different types of HTTP requests, and how to process and save data on a server.

---
### Web Interface
<img width="1920" height="928" alt="expressPCPCPC" src="https://github.com/user-attachments/assets/97a08e7f-1fa6-41b8-99a3-ec17440cb9b0" />

---
### App Interface
<img width="450" height="1000" alt="app_interface" src="https://github.com/user-attachments/assets/2956d17c-d89e-498f-b8d0-04d4a1c1c422" />

---
### Features
* **Cross-Platform Support:** Accepts data from both Android (Kotlin) and Web (HTML/JS) clients.
* **Text & Emoji Logging:** Converts numerical ratings into emojis and logs feedback with localized timestamps (IST).
* **Image Handling:** Supports receiving images via two methods:
  * `multipart/form-data` (Standard Android upload)
  * `Base64` encoded strings (Web Canvas upload)
* **Client-Side Validation:** JavaScript payload sanitization and keyword blocking.

## 🚀 Download App or visit site
You can download the pre-compiled APK directly from our [GitHub Releases](https://github.com/Xhaolean/Flask_Backend_PROJECT/releases/tag/Feedback) page.

OR visit this link to see it working [Express Yourself](https://https://aleznaor.pythonanywhere.com/) 

## Tech Stack
* **Backend:** Python, Flask, Flask-CORS, pytz, Werkzeug
* **Mobile Frontend:** Android Studio (Kotlin)
* **Web Frontend:** HTML5, CSS3, Vanilla JavaScript

## API Endpoints

The Flask backend exposes the following REST endpoints:

### 1. Web Feedback
* **URL:** `/websiterate`
* **Method:** `POST`
* **Payload:** JSON (`{ "name": "User", "rating": 5 }`)
* **Description:** Logs user feedback from the web interface into `feedback.txt`.

### 2. Android Feedback
* **URL:** `/rate`
* **Method:** `POST`
* **Payload:** JSON (`{ "username": "User", "expression": "😀" }`)
* **Description:** Logs user feedback from the mobile app into `response.txt`.

### 3. Web Image Upload
* **URL:** `/upload_base64`
* **Method:** `POST`
* **Payload:** JSON (`{ "image": "data:image/png;base64,..." }`)
* **Description:** Decodes a base64 string and saves it as a PNG in the `/images` directory.

### 4. Android Image Upload
* **URL:** `/upload_image`
* **Method:** `POST`
* **Payload:** `multipart/form-data` (File)
* **Description:** Securely saves an uploaded image file from the mobile app to the `/images` directory.

# Output Directory


## Setup & Installation

### Prerequisites
* Python 3.8+
* pip

### Running the Backend Locally
1. Clone the repository:
   ```
   git clone https://github.com/Xhaolean/Flask_backend_PROJECT.git
2. Navigate to the project directory:
   ```
   cd Xhaolean/Flask_backend_PROJECT
3. Install Dependencies 
   ```
   pip install Flask Flask-Cors pytz Werkzeug
4. Run the Flask Server
   ```
   python app.py
The server will start on http://0.0.0.0:5000/.
