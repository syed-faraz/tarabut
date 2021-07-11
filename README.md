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

 


The application has an API with the endpoint {BASE URL}/name exposed. 
The endpoint returns current date and time in the UAE timezone (Have used pytz to set the timezone to UAE) with values of the NAME and PASSWORD variables. 

•	The variable "NAME" takes its value from the Kubernetes Configmap
•	The variable "PASSWORD" takes its value from the Kubernetes Secret

Below is a screenshot of the API’s GET request and response in postman

 

Ingress:

I have setup nginx-controller and created the ingress resource using a test domain. 

 

If deploying locally, please set the test URL against localhost (127.0.0.1) inside your hosts file as shown below,
In this case, tarabut.example.com

 

In production environment, make sure to allow the access over the network with SSL certificates in place and set the DNS records for the application to be accessible over the internet.  

If deploying on a cloud platform, the service type can be set to 'loadbalancer' which will provision a load balancer with an external DNS record for access from the outside world. 


Other pre-requsities:
Docker
Kubernetes cluster
Kubectl

The other requirements are installed using pip through the requirements.txt file, which includes Flask and Flask-RESTful

pip/pip3 install -r requirements.txt

Build the Docker image using the below command,

docker build -t <tag> .

Deploy all the Kubernetes manifests using the below command,

kubectl 


Liveness and Readiness probes have been configured to perform health checks on the pod. 


RBAC:

NOTE: On Docker Desktop for mac, you will have to delete the ClusterRoleBinding, 'docker-for-desktop-binding', for the RBAC permissions to reflect. 
I have set the ClusterRole on the Service Account to only list the pods. No other action will be allowed. 

Once the RBAC files are deployed, in-order to test the permissions, you can switch the context to a test user by setting the token of the Service Account,

$ TOKEN=$(kubectl describe secrets "$(kubectl describe serviceaccount list-pods-sa -n tarabut| grep -i Tokens | awk '{print $2}')" -n tarabut | grep token: | awk '{print $2}')

$ kubectl config set-credentials test-user --token=$TOKEN

$ kubectl config set-context list-pods --cluster=docker-desktop --user=test-user

$ kubectl config use-context list-pods

Then run the below commands to check the permissions as seen in the screenshot below,

 

As you can see below, you can only list the pods in any namespace (cluster wide) but cannot do anything else. 
 


CICD:


 
