
from PIL import Image as pil_img
import numpy as np
import flask
from flask import render_template
from flask import request
from imagededup.methods import PHash
import uuid
import io
import pdb
import os

# initialize our Flask application and the Keras model
app = flask.Flask(__name__)
model = None
Dir_path = '/home/mubashir/MachineLearning/ML/rest_api/ARCHIVE/'

@app.route("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
        image_file = request.files["image"].read()
        file_name = request.files["image"].filename
        img_format = file_name.split('.')[1]
        img_name = file_name.split('.')[0]
        img_id = str(uuid.uuid1())
        img_name = img_name + '_' + img_id +'.'+ img_format
        image = pil_img.open(io.BytesIO(image_file))  
        if image:
            image.save( Dir_path + img_name)
            phasher = PHash()
            encodings = phasher.encode_images(image_dir=Dir_path)
            duplicates = phasher.find_duplicates(encoding_map=encodings)
            if duplicates[img_name]:
                os.remove(Dir_path + img_name) 
                pred = "This image already exists in the archive."
            else:
                pred = "Your image is saved to the archive."
        return render_template("index.html", pred='{}'.format(pred))
    return render_template("index.html", prediction=0)


# def load_model(image):
    # global model
    # model = load_learner('', 'Model_densenet121_new.pkl')
    # return model.predict(image)[0]


if __name__ == "__main__":
    app.run(port=5000, debug=True)
