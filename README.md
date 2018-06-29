# Celebrity-Face-Matcher
This repository will host code to match your face against a known celebrity. 

Aide-mémoire
1) Scrape web for celebrity images.
2) Standardize (Select up only the face) and resize (48x48)
3) Build a CNN using transfer learning, In Keras, Pytorch and train it, use Image Augmentation if needed.
4) Develop a Deep Learning Photo Caption Generator from Scratch
5) Create a web interface using Sanic or tornado to let users
    1) Upload image to match
    2) Add new celebrity, Note that this will require another training phase.
    3) Describe features of celebrity or your uploaded photo. (Wide lips, large forehead etc) It will use network in 4
6) For inference use TensorRT.
7) Create plot about which celebrity was matched most of the time. This specifies who has the most common face.
