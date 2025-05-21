# learning-oc
This repo is about learning the basics of how to deploy and app from scratch

Steps:
1. Build a simple app and test it locally.
2. Containerize it (using podman) and see that the container is also running properly.
3. Push it to [quay](https://quay.io/user/hacohen/?tab=repos).
4. Create a deployment in the [sandbox](https://console.redhat.com/openshift/sandbox) environment for RH developers. 
5. Create CI/CD for github and see that:
    1. The build and push actually creates a new tag in quay.
    2. You are able to deploy new versions of the app in OC.


## TODO
1. Make the app fail every X requests and see that OC is creating a new pod.
2. Overload the system with many requests and see that OC would create new pods to handle the requests.
3. Create another pod with postgress or mongoDB to store all the requests, alternativly, maybe use Volume.