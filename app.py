from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from datetime import datetime
import pytz
import os
import base64

app = Flask(__name__, template_folder='template')
CORS(app)  # Enable CORS

# Ensure the images folder exists
if not os.path.exists("images"):
    os.makedirs("images")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/websiterate', methods=['POST'])  # ****************WEBPAGE RATE*************
def rate():
    data = request.get_json()
    rating = data['rating']
    name = data['name']

    # Get the emoji based on the rating
    emojis = [
        "😒", "🤧", "🥱", "😐", "🙂", "😄", "😀", "😁", "😉", "😋", "👽"
    ]
    emoji = emojis[int(rating) - 1]  # Adjust index for 1-based rating

    # Set timezone to IST (GMT+5:30)
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)

    time_str = now.strftime("%I:%M %p")  # Format time as 12-hour clock with AM/PM
    date_str = now.strftime("%a %d %b")  # Format date as Day Mon Date (e.g., Mon 03 Feb)

    # Log the feedback with time and date into feedback.txt
    with open('feedback.txt', 'a') as f:
        f.write(f"{name} - {emoji} at {time_str} on {date_str}\n")

    return jsonify({'message': 'Feedback received'}), 200

@app.route('/upload_base64', methods=['POST'])
def upload_image():
    data = request.get_json()
    image_data = data.get('image')
    if not image_data:
        return jsonify({'message': 'No image data provided'}), 400

    try:
        # Expected format: "data:image/png;base64,...."
        header, encoded = image_data.split(",", 1)
        image_bytes = base64.b64decode(encoded)
    except Exception as e:
        return jsonify({'message': 'Failed to decode image data', 'error': str(e)}), 400

    # Save the image with a timestamp filename in the images folder
    filename = os.path.join("images", f"{datetime.now().strftime('%Y%m%d%H%M%S')}.png")
    try:
        with open(filename, "wb") as f:
            f.write(image_bytes)
    except Exception as e:
        return jsonify({'message': 'Error saving image', 'error': str(e)}), 500

    return jsonify({'message': 'Image uploaded successfully'}), 200


# ---------------- Mobile Feedback Endpoint ----------------
@app.route('/rate', methods=['POST'])
def save_feedback():
    """
    Endpoint for mobile app feedback.
    Expects a JSON payload with:
      - "username": the user's name
      - "expression": the emoji the user selected
    Appends the formatted feedback to response.txt.
    """
    data = request.get_json() or {}
    username = data.get("username", "Unknown User")
    expression = data.get("expression", "😐")

    # Get current IST time
    ist = pytz.timezone('Asia/Kolkata')
    now = datetime.now(ist)
    time_str = now.strftime("%I:%M %p")  # e.g., "08:20 PM"
    date_str = now.strftime("%d %b %A")   # e.g., "16 Feb Monday"

    formatted_response = f"{username} - {expression} at {time_str} on {date_str}"

    with open("response.txt", "a") as file:
        file.write(formatted_response + "\n")

    return jsonify({'message': 'Feedback saved!', 'status': 'success', 'data': formatted_response}), 200


#------------------------Mobile Capture Image ------------------------------#
from werkzeug.utils import secure_filename

@app.route('/upload_image', methods=['POST'])
def upload_image_android():
    """
    Accepts multipart/form-data image upload from Android app.
    Saves the uploaded image to the images/ folder with a timestamped filename.
    """
    if 'image' not in request.files:
        return jsonify({'message': 'No image part in the request'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'message': 'No file selected'}), 400

    filename = secure_filename(image.filename)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    saved_path = os.path.join("images", f"{timestamp}_{filename}")

    try:
        image.save(saved_path)
    except Exception as e:
        return jsonify({'message': 'Failed to save image', 'error': str(e)}), 500

    return jsonify({'message': 'Image uploaded successfully from Android', 'filename': saved_path}), 200




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
