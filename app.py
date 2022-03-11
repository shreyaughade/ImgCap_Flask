from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from PIL import Image
import os

port = int(os.environ.get('PORT', 5000))
UPLOAD_FOLDER = os.getcwd() + "/images"
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
  return jsonify({"message": "Hello"})

@app.route("/uploadImage", methods=["POST"])
def upload():
  file = request.files['image']
  img = Image.open(file.stream)
  return jsonify({'message': 'success', 'size': [img.width, img.height]})
    # if request.method == "POST":
        # print(request)
        # image = request.files["image"]
        # filename = secure_filename(image.filename)
        # return jsonify({"message":"hi"})
        # print(filename)
        # image.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        # return jsonify({"message": "Image Uploaded Successfully"})


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = port, debug=True)


# @app.route('/predict', methods=['POST'])
# def predict():
#  lr = joblib.load("model.h5")
#  with open(static_dir+'sample.jpg',"wb") as fh:
#             fh.write(base64.decodebytes(request.data))
#         captions=gc.generate_captions(static_dir+'sample.jpg')
#         cap={"captions":captions}
#         with open("text/data.json","w") as fjson:
#                     json.dump(cap,fjson)
