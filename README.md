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
6. I made the app crush every 5 requests an saw that the a new pod has been deployed - I also wanted to implement a scaling but due to what seems to be a firewall that is in use on the SB environment I wasn't able to overload the system enough.


## TODO
1. Create another pod with postgress or mongoDB to store all the requests, alternativly, maybe use Volume.