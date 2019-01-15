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


DOCKER-Stuff

1) docker build -t celebrity:latest .
2) docker run -p 5000:5000 celebrity:latest
OR
docker run -p 5000:5000 <IMAGE_ID>

3) docker tag celebrity:latest nvcr.io/celebs:latest
// I do not have access to nvcr for pushing as I do not own
// DGX,DGX-1,DGX-2

4) docker login nvcr.io

5) docker push nvcr.io/celebs:latest

nvcr allows you to pull the image
So, your dockerfile will have
FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

Then follow steps 1,2,3,4 off course changing nvcr.io to either
1) ecr
2) gcr
3) docker hub
4) private-registry

FOR LOCALHOST

docker tag celebrity:latest localhost:5000/celebrity:latest
docker run -ti localhost:5000/celebrity:latest

