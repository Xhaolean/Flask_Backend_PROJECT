# Android & Web to Flask Backend Integration

## About The Project
This open-source project demonstrates how to connect front-end applications—specifically an Android app built with Kotlin and a standard HTML/JS website—to a Python backend. It is designed to help beginners understand how backend REST APIs work, how to handle different types of HTTP requests, and how to process and save data on a server.

### Features
* **Cross-Platform Support:** Accepts data from both Android (Kotlin) and Web (HTML/JS) clients.
* **Text & Emoji Logging:** Converts numerical ratings into emojis and logs feedback with localized timestamps (IST).
* **Image Handling:** Supports receiving images via two methods:
  * `multipart/form-data` (Standard Android upload)
  * `Base64` encoded strings (Web Canvas upload)
* **Client-Side Validation:** JavaScript payload sanitization and keyword blocking.

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

## Setup & Installation

### Prerequisites
* Python 3.8+
* pip

### Running the Backend Locally
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
