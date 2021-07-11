# Tarabut

Application 

I have created the application with the API endpoint, using Python and Flask.
•	The application has been containerized using Docker.
•	The build and push of Docker Image is automated through Github Action which gets triggered for every git push. 
•	The deployment is done on Kubernetes cluster using the Kubernetes manifest files. 

The Docker Image has been prebuilt and made available for deployment on the public Dockerhub repository,
 
docker pull faraaz/tarabut:v1.0.0

To deploy the application on a Kubernetes cluster, you can clone the repository and run the below commands,

NOTE: Please create a namespace with the name, ‘tarabut’, for the deployment to be successful.

1.	kubectl create ns tarabut 
2.	kubectl apply -f kubernetes/

Where Kubernetes is the name of the folder containing all the manifest files.

At this stage, the deployment should be successful and the application pod should be running as seen in the below screenshot.

<img width="532" alt="Screen Shot 2021-07-11 at 7 59 57 AM" src="https://user-images.githubusercontent.com/45511087/125181512-1fca0c80-e223-11eb-924b-15ec90797f49.png">

The application has an API with the endpoint {BASE URL}/name exposed. 
The endpoint returns current date and time in the UAE timezone (Have used pytz to set the timezone to UAE) with values of the NAME and PASSWORD variables. 

•	The variable "NAME" takes its value from the Kubernetes Configmap
•	The variable "PASSWORD" takes its value from the Kubernetes Secret

Below is a screenshot of the API’s GET request and response in postman

<img width="1013" alt="Screen Shot 2021-07-10 at 6 40 14 PM" src="https://user-images.githubusercontent.com/45511087/125181546-759eb480-e223-11eb-9444-0196afffc1da.png">

Ingress:

I have setup nginx-controller and created the ingress resource using a test domain. 

<img width="559" alt="Screen Shot 2021-07-09 at 9 07 09 PM" src="https://user-images.githubusercontent.com/45511087/125181600-f067cf80-e223-11eb-814e-a01d176e807c.png">

If deploying locally, please set the test URL against localhost (127.0.0.1) inside your hosts file as shown below,
In this case, tarabut.example.com

<img width="294" alt="Screen Shot 2021-07-10 at 6 35 03 PM" src="https://user-images.githubusercontent.com/45511087/125181611-30c74d80-e224-11eb-93fe-edf33a71e61a.png">


In production environment, make sure to allow the access over the network with SSL certificates in place and set the DNS records for the application to be accessible over the internet.  

If deploying on a cloud platform, the service type can be set to 'loadbalancer' which will provision a load balancer with an external DNS record for access from the outside world. 


RBAC:

NOTE: On Docker Desktop for mac, you will have to delete the ClusterRoleBinding, 'docker-for-desktop-binding', for the RBAC permissions to reflect. 
I have set the ClusterRole on the Service Account to only list the pods. No other action will be allowed. 

Once the RBAC files are deployed, in-order to test the permissions, you can switch the context to a test user by setting the token of the Service Account,

$ TOKEN=$(kubectl describe secrets "$(kubectl describe serviceaccount list-pods-sa -n tarabut| grep -i Tokens | awk '{print $2}')" -n tarabut | grep token: | awk '{print $2}')
$ kubectl config set-credentials test-user --token=$TOKEN
$ kubectl config set-context list-pods --cluster=docker-desktop --user=test-user
$ kubectl config use-context list-pods

Then run the below commands to check the permissions as seen in the screenshot below,

<img width="633" alt="Screen Shot 2021-07-11 at 1 00 08 AM" src="https://user-images.githubusercontent.com/45511087/125181640-813eab00-e224-11eb-9c84-f7c7b42b30b3.png">


As you can see below, you can only list the pods in any namespace (cluster wide) but cannot do anything else. 
 
<img width="1107" alt="Screen Shot 2021-07-11 at 1 03 26 AM" src="https://user-images.githubusercontent.com/45511087/125181649-974c6b80-e224-11eb-9317-165a9dd64765.png">


CICD:

<img width="1414" alt="Screen Shot 2021-07-11 at 8 28 23 AM" src="https://user-images.githubusercontent.com/45511087/125181659-aa5f3b80-e224-11eb-931f-e4d210bb6778.png">

 
