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

------------------------------Putting on dockerhub-------------------------
docker login
docker tag localhost:5000/celebrity:latest ishanbhatt/celebrity:latest
docker push ishanbhatt/celebrity:latest


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

KUBERNETES NOTES:-

1) minikube start --docker-env HTTP_PROXY=$http_proxy --docker-env HTTPS_PROXY=$https_proxy --docker-env NO_PROXY=$no_proxy --insecure-registry MY_IP:5000
2) kubectl create -f Celeb_Matcher_namespace.yaml
3) kubectl create -f Celeb_Matcher.yaml
4) kubectl get deployments --namespace=celeb (Need to run it to get name of deployment)
5) kubectl expose deployment celeb-matcher --namespace=celeb --port=5000 --type=NodePort
OR
5) kubectl create -f Celeb_Matcher_service.yaml
6) minikube ip -> <IP_ADDRESS>
7) curl -X POST -F image=@anu2.jpg 'http://<IP_ADDESS>:30080/predict'

More coming up for ClusterIP,LoadBalancer(Not supported in minikube), Ingress

