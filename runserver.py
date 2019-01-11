
# coding: utf-8

# In[22]:


from keras.models import model_from_json
from keras.preprocessing import image
from flask import Flask, request, jsonify
import numpy as np
import os
from PIL import Image
import io
import tensorflow as tf

# # Here we will define globals

# In[20]:


app = Flask(__name__)
model = None
UPLOAD_FOLDER = "Uploaded"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# actress_names = [item.split("/")[-2] for item in sorted(glob("../Celebs/train/*/"))]
actress_names = ["anushka","deepika","jaq","kat","priyanka"]

# ## Load the model

# In[16]:


def load_model(json_model):
    global model
    json_file = open(json_model)
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    model.load_weights('weights.best.vgg19_2.hdf5')


# In[17]:


def path_to_VGG19_feature(img_path):
    img = img_path.resize((224,224))
    tensor = np.expand_dims(image.img_to_array(img), axis=0)
    tensor = tensor.astype("float32")/255
    return tensor


# In[23]:


def get_next_name(actress_name):
    actress_files = os.listdir(UPLOAD_FOLDER)
    counter = 0
    for file_name in actress_files:
        if file_name.startswith(actress_name):
            counter += 1
    if counter > 0:
        return actress_name+str(counter+1)
    else:
        return actress_name+"0"


# In[24]:


@app.route("/predict", methods=["POST"])
def predict():
    image = request.files["image"]
    image_bytes = Image.open(io.BytesIO(image.read()))
    tensor = path_to_VGG19_feature(image_bytes)
    global graph
    with graph.as_default():
        predicted_vector = model.predict(tensor)
    actress_name = actress_names[np.argmax(predicted_vector)]
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], get_next_name(actress_name)))
    return jsonify("You look like {}".format(actress_name))


# In[26]:
"""
The lines related to tf in main and predict are critical.
It makes sure that allof your threads are using the same graph object.
Otherwise you will end up having 1) graph to load models and 2) To infer.
https://github.com/keras-team/keras/issues/2397
"""
if __name__ == '__main__':
    load_model('new_model_66_test.json')
    graph = tf.get_default_graph()
    app.run(host="0.0.0.0")


