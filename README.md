# Celebrity-Face-Matcher
This repository will host code to match your face against a known celebrity. 

Aide-mémoire
1) Scrape web for celebrity images.
2) Standardize (Select up only the face) and resize (48x48)
3) Build a CNN using transfer learning, In Keras, Pytorch and train it, use Image Augmentation if needed.
4) Create a web interface using Sanic or tornado to let users
    1) Upload image to match
    2) Add new celebrity, Note that this will require another training phase.
5) For inference use TensorRT.
6) Create plot about which celebrity was matched most of the time. This specifies who has the most common face.
    1) Y- Axis names, Vertical Plotes BAR Charts
    2) Click on any of the BAR and that will let you see all the images.
