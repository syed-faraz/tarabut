# tarabut

I have created the application with the API, using Python and Flask.
The deployment is through Kubernetes manifest files. 
The build of Docker Image is automated through Github Action which gets triggered for every push. 

If building the Docker image locally, install the pre-requisites 
python
pip

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

The application has an API with the endpoint {BASE URL}/name exposed. 
The endpoint returns current date and time in the UAE timezone with values of the NAME and PASSWORD variables. 

The variable "NAME" takes its value from the Configmap at the time of deployment from the Kubernetes manifest
The variable "PASSWORD" takes its value from the secret at the time of deployment from the Kubernetes manifest

Have used pytz to set the timezone to UAE


If deploying locally, please set the test URL against localhost (127.0.0.1) inside your hosts file as shown below,
For example, tarabut.example.com/name

If deploying on cloud, the service type can be set to 'loadbalancer' which will provision a load balancer for access from the outside world. 

The application has been containerized using Dockerfile. 
The Docker image gets built and pushed by the Github Action which gets triggered for every push to the main branch.

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


