# from flask import Flask, request, jsonify
# import base64
# import requests

# app = Flask(__name__)

# API_KEY = "hehehe put y"
# API_URL = "https://api.openai.com/v1/chat/completions"

# @app.route("/describe", methods=["POST"])
# def describe_image():
#     if "image" not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400

#     image_file = request.files["image"]
#     image_bytes = image_file.read()
#     image_base64 = base64.b64encode(image_bytes).decode("utf-8")

#     headers = {
#         "Authorization": f"Bearer {API_KEY}",
#         "Content-Type": "application/json"
#     }

#     payload = {
#         "model": "gpt-4.1-mini",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": "Describe this image."},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{image_base64}"
#                         }
#                     }
#                 ]
#             }
#         ]
#     }

#     response = requests.post(API_URL, headers=headers, json=payload)
#     result = response.json()

#     description = result["choices"][0]["message"]["content"]

#     return jsonify({"description": description})

# if __name__ == "__main__":
#     app.run(debug=True



# ////////////////////////////////////////////xc cnckcnkcckckc///////////





# ///////this is right approch just go in postman post it and it will work http://127.0.0.1:5000/describe//////////////////////////
# from flask import Flask, request, jsonify
# import base64
# from openai import OpenAI

# app = Flask(__name__)

# client = OpenAI(api_key="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")

# @app.route("/describe", methods=["POST"])
# def describe_image():
#     if "image" not in request.files:
#         return jsonify({"error": "No image uploaded"}), 400

#     image_file = request.files["image"]
#     image_bytes = image_file.read()
#     image_base64 = base64.b64encode(image_bytes).decode("utf-8")

#     response = client.chat.completions.create(
#         model="gpt-4.1-mini",
#         messages=[
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": "Describe this image in one short sentence."},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": f"data:image/jpeg;base64,{image_base64}"
#                         }
#                     }
#                 ]
#             }
#         ]
#     )

#     description = response.choices[0].message.content
#     return jsonify({"description": description})

# if __name__ == "__main__":
#     app.run(debug=True)


# new approch offline through python sdk


from flask import Flask, request, jsonify
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

app = Flask(__name__)

# Load model once (this may take some time first time)
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

@app.route("/describe", methods=["POST"])
def describe_image():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    image = Image.open(image_file).convert("RGB")

    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return jsonify({"description": caption})

if __name__ == "__main__":
    app.run(debug=True)




